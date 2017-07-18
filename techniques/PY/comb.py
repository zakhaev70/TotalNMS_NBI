import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'
ns = {'soap':'http://schemas.xmlsoap.org/soap/envelope/'}  # namespaces for path traversal

with requests.Session() as s:
    s.auth=('admin','manager')
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})

    with open('/src/XMLReqs/getCPEsByManagedGroup.xml','r') as f:
        body = f.read()

    r = s.post(host+'/cpeService', data=body)
    print(r)

    print('-'*60)   
    ret = ET.fromstring(r.text)[0][0][0]
    print('Total number of CPEs found:', ret.find('totalNumber').text)

    with open('/src/XMLReqs/getCPEpartNumber.xml','r') as f:
        body2 = ET.fromstring(f.read())

    for cpe in ret.find('cpes')[:20]:
        managedGroupId = cpe.find('cpeId/managedGroupId').text
        subscriberId = cpe.find('cpeId/subscriberId').text
        body2[1][0].find('id/managedGroupId').text = managedGroupId
        body2[1][0].find('id/subscriberId').text = subscriberId
        r2 = s.post(host+'/cpeService', data=ET.tostring(body2))
        #print(r2.text)
        #print('|->',ET.tostring(body2))
        ret2 = ET.fromstring(r2.text)[0][0][0]
        #print(ret2)
        partNumber = [(item.tag,item.text) for item in ret2]
        print(managedGroupId, subscriberId,partNumber)
