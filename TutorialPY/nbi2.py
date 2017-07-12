import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'
ns = {'ns3':'urn:com.gilat.ngnms.server.ws.dto.cfg'}  #namespaces for find()

with requests.Session() as s:
    s.auth=('admin','manager')
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 
            'SOAPAction': '', 'Connection': 'keep-alive'})

    with open('../XMLReqs/getCPEsByManagedGroup.xml','r') as f:
        body = f.read()

    r = s.post(host+'/cpeService', data=body)
    print(r)  #response object
    print('-'*60)   

    resp = ET.fromstring(r.text)  #creates XML element
    print(resp)  #ElementTree object
    print('-'*60)
    numcpes = resp[0][0].find('return/totalNumber')
    print(numcpes.tag, numcpes.text, sep=': ')
    print('-'*60)
    cpelist = resp[0][0][0].find('cpes')
    for i in range(len(cpelist)):
        print("CPE #{}'s physical port's supported vlanId: ".format(i+1), 
                cpelist[i].find('physPorts/ns3:PhysicalPort/supportedVRs/vlanID',ns).text)

