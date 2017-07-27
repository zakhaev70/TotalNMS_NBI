import requests
import xml.etree.ElementTree as ET
import NBI
import csv
from datetime import datetime

### Commands ###
#Returns initial RF Audit of all CPEs in a MG
def initialRFAudit(session, mgid, opState='all', pretty=True):
    with open(NBI.sitepath('/src/XMLReqs/getCPEsByManagedGroup.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)
    cpesRF, hasMore, lastIndex = [], True, '0'
    while hasMore:
        req[1][0].find('managedGroupId').text = str(mgid)
        req[1][0].find('lastIndex').text = lastIndex
        r = session.post(NBI.host+'/cpeService', data=ET.tostring(req))
        resp = ET.fromstring(r.text)
        isfault = NBI.isFault(resp)
        if isfault:
            return isfault['faultstring']
        else:
            ret = resp[0][0].find('return')
            hasMore, lastIndex = 'true'==ret.find('hasMore').text.lower(), ret.find('lastIndex').text
            for cpe in ret.find('cpes'):
                state = cpe.find('operationalState').text
                if state.lower()==opState.lower() or opState=='all':
                    RFAudits = [[field.text for field in cpe.find('serviceActivationRFAudit')]]
                    otherAudit = [field.text for field in cpe.find('otherRFAudit')]
                    if otherAudit and otherAudit[-3]!=RFAudits[0][-3]:
                        RFAudits.append(otherAudit)
                    if pretty:
                        for RFAudit in RFAudits:
                            if RFAudit[0]!='0':
                                for i in range(1,7):
                                    RFAudit[i] = '{} dB'.format(int(RFAudit[i])/10)
                                RFAudit.extend([0,0])
                                RFAudit[-1] = RFAudit[-3]
                                start, end = int(RFAudit[-5]), int(RFAudit[-4])
                                startdate = datetime.utcfromtimestamp(start)
                                RFAudit[-5] = '{:02}/{:02}/{}'.format(startdate.day,startdate.month,startdate.year)
                                RFAudit[-4] = '{:02}:{:02}:{:02}'.format(startdate.hour,startdate.minute,startdate.second)
                                enddate = datetime.utcfromtimestamp(end)
                                RFAudit[-3] = '{:02}/{:02}/{}'.format(enddate.day,enddate.month,enddate.year)
                                RFAudit[-2] = '{:02}:{:02}:{:02}'.format(enddate.hour,enddate.minute,enddate.second)
                    cpesRF.append([cpe.find('cpeId/subscriberId').text, state, RFAudits])
    return cpesRF

### Main for debugging purposes ###
if __name__=='__main__':
    import sys, os
    with requests.Session() as s:
        s.auth=(NBI._username, NBI._password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})
        
        mgid = input('Enter MG ID: ')
        if not mgid:  #default to 6
            mgid = '6'
        print('Working...',end='\r')

        headerrow = ['subscriberId','operationalState','Status','RTN CoPol C/N','RTN Cross-Pol C/N',
                    'RTN Co/Cross-Pol Delta','FWD Rx Es/N0','IB Threshold','OB Threshold','Start Date',
                    'Start Time', 'End Date', 'End Time','Attenuator P1 dB']
        irfa = initialRFAudit(s, mgid)

        filepath = NBI.sitepath('/functions/RFAuditResults')
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filename = os.path.join(filepath, 'RFAudit{}.csv'.format(mgid))
        with open(filename, 'w') as csvf:
            csvw = csv.writer(csvf)
            csvw.writerow(headerrow)
            for cpeRF in sorted(irfa, key=lambda x: x[0]):
                csvw.writerow(cpeRF[:2] + cpeRF[2][0])
                for RFAudit in cpeRF[2][1:]:
                    csvw.writerow(['',''] + RFAudit)
        print('Done. Results written to', filename)
