import requests
import xml.etree.ElementTree as ET

host = 'http://172.19.254.3/ws'
ns = {'soap':'http://schemas.xmlsoap.org/soap/envelope/'}  # namespaces for path traversal

def isFault(resp):
    if type(resp) is not ET.Element:
        resp = ET.fromstring(resp)  #then, it's string
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

def numOnlineByMGId(session, mgid):
    with open('../src/XMLReqs/getNumberOfActiveCPEs.xml','r') as f:
        body = f.read()
    req = ET.fromstring(body)
    req[1][0].find('managedGroupId').text = str(mgid)

    r = session.post(host+'/elementsInformationService', data=ET.tostring(req))
    resp = ET.fromstring(r.text)
    isfault = isFault(resp)
    if isfault:
        return isfault['faultstring']
    else:
        return resp[0][0].find('return').text

if __name__=='__main__':
    with requests.Session() as s:
        s.auth=('admin','manager')
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
        
        for i in range(1,15):
            print(i, numOnlineByMGId(s, i), sep=': ')
