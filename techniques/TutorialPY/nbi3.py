import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'

with requests.Session() as s:
    s.auth=('admin','manager')
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 
            'SOAPAction': '', 'Connection': 'keep-alive'})

    with open('../../src/XMLReqs/getCPEsByManagedGroup.xml','r') as f:
        body = f.read()

    mgid = input('Enter Managed Group ID: ')
    assert(mgid.isdigit())
    xmlbody = ET.fromstring(body)
    xmlbody[1][0][0].text = mgid  #managedGroupId tag gets new value
    body = ET.tostring(xmlbody)

    r = s.post(host+'/cpeService', data=body)
    resp = ET.fromstring(r.text)
    numcpes = resp[0][0].find('return/totalNumber')
    print(numcpes.tag, numcpes.text, sep=': ')
  
