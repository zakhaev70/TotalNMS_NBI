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

#Returns dict with fault info if true, else None
def isFault(resp):
    if type(resp) is not ET.Element:
        if type(resp) is requests.Response:
            resp = resp.text
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

def isMG(mgid):
    with requests.Session() as s:
        s.auth=(_username, _password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
        with open(sitepath('/src/XMLReqs/getNumberOfActiveCPEs.xml'),'r') as f:
            body = f.read()
        req = ET.fromstring(body)
        req[1][0].find('managedGroupId').text = str(mgid)

        r = s.post(host+'/elementsInformationService', data=ET.tostring(req))
        return not isFault(r) 

#Might take a few seconds to execute
def allMGs(start=0, verbose=False, keepVerbose=False):
    with requests.Session() as s:
        s.auth=(_username, _password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
        i, outofrange, goneinrange = 0, True, False
        mgs = []
        with open(sitepath('/src/XMLReqs/getNumberOfActiveCPEs.xml'),'r') as f:
            body = f.read()
        req = ET.fromstring(body)
        while not outofrange or (outofrange and not goneinrange):
            if verbose:
                print('--allMGs(): Checking mgid #{}... Currently {}    '.format(i, 
                        'out of range' if outofrange else 'in range'), end='\r')
            req[1][0].find('managedGroupId').text = str(i)
            r = s.post(host+'/elementsInformationService', data=ET.tostring(req))
            isfault = isFault(r)
            if isfault:
                if isfault['businessFaultTypeCode'] == '7': #out of range
                    outofrange = True
            else:
                outofrange = False
                goneinrange = True
                mgs.append(i)
            i+=1    
        if verbose:
            if keepVerbose:
                print('--allMGs(): Process finished at id #', i, sep='', end=(' '*20)+'\n')
            else:
                print(' '*50, end='\r')
        return mgs

### Main for debugging purposes ###
if __name__=='__main__':
    import sys
    with requests.Session() as s:
        s.auth=(_username, _password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
       
        for i in allMGs(verbose=True,keepVerbose=True):
            print(i, isMG(i), sep=': ')
