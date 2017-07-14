#! /usr/bin/env python3
#
# Javier Sorribes, Hispasat S.A.
# 05/07/2017
#
# Server to connect to Gilat's SkyEdge II-c NBI, accounting for CORS (preflight and redirect)
# Includes 'Access-Control-Allow-Origin' headers and more
# Must send authorization credentials as header
#
# Tested with JavaScript and other Python3 applications

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import time
from base64 import b64decode
import xml.etree.ElementTree as ET

HOST_ADDR = '127.0.0.1'  #localhost
PORT_NUMBER = 9000

class NBIConnHandler(BaseHTTPRequestHandler):   
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        message = '''<h1>Welcome to Pre-NBI Server</h1>
        <p>This is a intermediary server between you and Gilat's NBI</p>
        <p>It accounts for CORS. Submit POST requests at your will!</p>'''
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        auth = self.headers['Authorization']
        if auth:
            if ' ' in auth:  #there is a descriptor before the credentials
                auth = auth[auth.index(' ')+1:]  #like 'Basic ', for example
            username, password = str(b64decode(auth),'utf-8').split(':') #decode from ascii
        else:  #credentials were not given
            print('--Authorization required to access NBI')
            username, password = None, None
        response = self.post_NBI(body, username, password)  #post request sent to NBI
        self.send_response(response.status_code)
        for h,v in response.headers.items():
            if h.lower() not in ['date', 'server']:  #automatically provided by our server
                self.send_header(h,v)
        self.send_header('Access-Control-Allow-Origin', self.headers['Origin'])
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()
        self.wfile.write((response.text).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', self.headers['Origin'])  #or '*' for all origins
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', self.headers['Access-Control-Request-Headers'])
        #self.send_header('Access-Control-Max-Age', '86400')  #OPTIONS req cached for 24h
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()

    def post_NBI(self, body, username='', password=''):
        host = 'http://172.19.254.3/ws'
        nbiwsdls = ['cpeService', 'qosService', 'elementsInformationService', 'multiCastService']
        with requests.Session() as s:
            s.auth=(username,password)
            s.headers.update(self.headers)
            for service in nbiwsdls:  #try all wsdls until right one
                response = s.post(host+'/'+service, data=body)
                if response.status_code!=500 or ET.fromstring(response.text)[0][0].find('detail') is not None:
                    break  #only continue if command not in service (status_code 500 and XML response has no detail in fault)
            else:
                print('--NBI command not found')  #could maybe return xml message instead
        return response

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_ADDR, PORT_NUMBER), NBIConnHandler)
    print(time.asctime(), 'Server Starts - {}:{}'.format(HOST_ADDR, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('\r'+time.asctime(), 'Server Stops  - {}:{}'.format(HOST_ADDR, PORT_NUMBER))
