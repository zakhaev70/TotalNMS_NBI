import requests
import xml.etree.ElementTree as ET
import json, os.path as OP

### Setting up global variables ###
#the root directory:
root = OP.normpath(OP.join(OP.dirname(OP.abspath(__file__)),'..')).replace('\\','/').replace('//','/')
host = 'http://172.19.254.3/ws'
_username, _password = 'admin', 'manager'
with open(OP.normpath(OP.join(root,'src/ns.json')), 'r') as nsjson:
    ns = json.load(nsjson)  # namespaces for path traversal

### Helpers ###
def sitepath(path):
    return OP.normpath('/'.join([root, path]))

def isFault(resp):
    if type(resp) is not ET.Element:
        resp = ET.fromstring(resp)  #then, it's string
    try: 
        fault = resp[0].find('soap:Fault',ns)
        if fault:
            ret = {'faultcode': fault.find('faultcode').text,
                    'faultstring': fault.find('faultstring').text}
            detail = fault.find('detail') 
            if detail:
                ret['businessFaultTypeCode'] = detail[0].find('businessFaultTypeCode').text
            return ret
        else:
            return None
    except ET.ParseError:  #resp not fault xml
        return None

### Commands ###
def numOnlineByMGId(session, mgid):
    with open(sitepath('/src/XMLReqs/getNumberOfActiveCPEs.xml'),'r') as f:
        body = f.read()
    print(body)
    return
    req = ET.fromstring(body)
    req[1][0].find('managedGroupId').text = str(mgid)

    r = session.post(host+'/elementsInformationService', data=ET.tostring(req))
    resp = ET.fromstring(r.text)
    isfault = isFault(resp)
    if isfault:
        return isfault['faultstring']
    else:
        return resp[0][0].find('return').text

### Main for debugging purposes ###
if __name__=='__main__':
    with requests.Session() as s:
        s.auth=(_username, _password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
        
        for i in range(1,15):
            print(i, numOnlineByMGId(s, i), sep=': ') 
