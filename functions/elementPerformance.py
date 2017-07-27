import requests
import xml.etree.ElementTree as ET
import NBI
import time
from datetime import datetime

### Commands ###

#Returns the performance a CPE
def CPEPerformance(session,mgid, subsid,reportType,resolution='FM',start=(int(time.time())-10000)*1000,end=int(time.time())*1000):
    with open(NBI.sitepath('/src/XMLReqs/getElementPerformance.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)
    reportElement = req[1][0].find('reportElement')
    reportElement.find('element/eType').text = 'CPE'
    reportElement.find('element/cpeId/managedGroupId').text = str(mgid)
    reportElement.find('element/cpeId/subscriberId').text = str(subsid)
    reportElement.find('reportType').text = reportType
    reportElement.find('resolution').text = resolution
    reportElement.find('startDate').text = str(start-start%300)
    reportElement.find('endDate').text = str(end-end%300)
    req[1][0].find('lastIndex').text = '0'
    r = session.post(NBI.host+'/elementsInformationService', data=ET.tostring(req))
    resp = ET.fromstring(r.text)
    isfault = NBI.isFault(resp)
    if isfault:
        return isfault['faultstring']
    else:
        ret = resp[0][0].find('return')
        return [(x.text, y.text) for x,y in ret.findall('series/ns4:Series/points/ns4:Point', NBI.ns)]
   
#Returns the performance info of all CPEs in a MG
def MGPerformance(session,mgid,reportType,resolution='FM',start=(int(time.time())-10000)*1000,end=int(time.time())*1000):
    with open(NBI.sitepath('/src/XMLReqs/getElementPerformance.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)
    reportElement = req[1][0].find('reportElement')
    reportElement.find('element/eType').text = 'MANAGED_GROUP'
    reportElement.find('element/eId').text = str(mgid)
    reportElement.find('reportType').text = reportType
    reportElement.find('resolution').text = resolution
    reportElement.find('startDate').text = str(start)  #in miliseconds
    reportElement.find('endDate').text = str(end)
    report, hasMore, lastIndex = {}, True, '0'
    while hasMore:
        req[1][0].find('lastIndex').text = lastIndex
        r = session.post(NBI.host+'/elementsInformationService', data=ET.tostring(req))
        resp = ET.fromstring(r.text)
        isfault = NBI.isFault(resp)
        if isfault:
            return isfault['faultstring']
        else:
            ret = resp[0][0].find('return')
            hasMore, lastIndex = 'true'==ret.find('hasMore').text.lower(), ret.find('lastIndex').text
            for series in ret.findall('series/ns4:Series', NBI.ns):
                points = [(x.text, y.text) for x,y in series.findall('points/ns4:Point', NBI.ns)]
                report[series.find('element/cpeId/subscriberId').text] = points
    return report  #dictionary with performance for each CPE

def lastMGPerformance(session, mgid, reportType, onlyOnline=True):
    sample = CPEPerformance(session,2,2,reportType)
    lastTime = sample[-1][0]
    allperf = MGPerformance(session,mgid,reportType,start=lastTime)
    newd = {}
    for sid,p in allperf.items():
        if p:
            newd[sid] = p[0][1]
        elif not onlyOnline:
            newd[sid] = None
    return [lastTime, newd]

def prettyLastMGPerformance(session, mgid, reportType, onlyOnline=True):
    ret = lastMGPerformance(session,mgid,reportType, onlyOnline)
    stringy = 'Results for MG #{} at {} UTC'.format( mgid, datetime.utcfromtimestamp(int(ret[0])/1000) )
    maxlen = max(len('subscriberId'), len(reportType))
    stringy += '\n' + '|'.join(map(lambda x: x.center(maxlen), ['subscriberId',reportType]))
    headlen = len(stringy)
    for sid in sorted(ret[1].keys()):
        val = ret[1][sid] if ret[1][sid] else '-'
        stringy += '\n' + '|'.join(map(lambda x: x.center(maxlen), [str(sid),str(val)+'dB']))
            
    return stringy

### Main for debugging purposes ###
if __name__=='__main__':
    import sys
    with requests.Session() as s:
        s.auth=(NBI._username, NBI._password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
    
        mgid = input('Enter MG Id: ')
        print(prettyLastMGPerformance(s, mgid if mgid else 6, 'LAST_FWD_RX_ESN0'))
        print('-'*40)
        print(prettyLastMGPerformance(s, mgid if mgid else 6, 'TX_CAPABILITY'))
        
