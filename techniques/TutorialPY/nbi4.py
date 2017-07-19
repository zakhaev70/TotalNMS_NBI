import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'

with requests.Session() as s:
    s.auth=('admin','manager')
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 
            'SOAPAction': '', 'Connection': 'keep-alive'})

    with open('../../src/XMLReqs/getCPEsByManagedGroup.xml','r') as f:
        body = f.read()
    with open('../../src/XMLReqs/getCPEVolumes.xml','r') as f2:
        body2 = f2.read()

    mgid = input('Enter Managed Group ID: ')
    assert(mgid.isdigit())
    xmlbody = ET.fromstring(body)
    xmlbody[1][0][0].text = mgid  #managedGroupId tag gets new value
     
    r = s.post(host+'/cpeService', data=ET.tostring(xmlbody))
    resp = ET.fromstring(r.text)
    cpes = resp[0][0].find('return/cpes')
    
    print("CPEs' Consumed Volume for MG", mgid)
    xmlbody2 = ET.fromstring(body2)
    xmlbody2[1][0][0][0].text = mgid  #MG Id same for all CPEs
    for cpe in cpes:
        subsid = cpe[0][1].text
        xmlbody2[1][0][0][1].text = subsid  #subscriber Id set
        r2 = s.post(host+'/qosService', data=ET.tostring(xmlbody2))
        resp2 = ET.fromstring(r2.text)
        print('CPE #{}:'.format(subsid), 
                resp2[0][0].find('return/consumed/cmbQuota').text)

