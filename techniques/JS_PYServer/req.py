import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'
ns = {'soap':'http://schemas.xmlsoap.org/soap/envelope/'}  # namespaces for path traversal

with requests.Session() as s:
    s.auth=('admin','manager')
    #s.verify = False  # only needed if https with no SSL certificate
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
    #print(s.headers)

    with open('/src/XMLReqs/getCPEpartNumber.xml','r') as f:
        body = f.read()

    #r = s.post(host+'/cpeService', data=body)
    r = s.post('http://127.0.0.1:9000', data=body)
    print(r)

    print('-'*60)   
    resp = ET.fromstring(r.text)
    print(resp)
    print(resp[0][0].find('return/factoryPartNumber').text)
    for item in resp[0][0][0]:
        print(item.tag, item.text)

    print('-'*60)
    print('\n'.join(x+': '+y for x,y in r.headers.items()))
