import requests
import xml.etree.ElementTree as ET
import NBI

### Commands ###
#Returns the total number of CPEs in a MG
def numCPEsInMG(session, mgid):
    with open(NBI.sitepath('/src/XMLReqs/getCPEsByManagedGroup.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)
    req[1][0].find('managedGroupId').text = str(mgid)
    req[1][0].find('lastIndex').text = '0'

    r = session.post(NBI.host+'/cpeService', data=ET.tostring(req))
    resp = ET.fromstring(r.text)
    isfault = NBI.isFault(resp)
    if isfault:
        return isfault['faultstring']
    else:
        return resp[0][0].find('return/totalNumber').text

#Return the total number of CPEs online in a MG
def numCPEsOnlineInMG(session, mgid):
    with open(NBI.sitepath('/src/XMLReqs/getNumberOfActiveCPEs.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)
    req[1][0].find('managedGroupId').text = str(mgid)

    r = session.post(NBI.host+'/elementsInformationService', data=ET.tostring(req))
    resp = ET.fromstring(r.text)
    isfault = NBI.isFault(resp)
    if isfault:
        return isfault['faultstring']
    else:
        return resp[0][0].find('return').text

#Returns the number of CPEs in each operational state in a MG
def allCPEsOpStateInMG(session, mgid, verbose=False):
    if verbose:
        print('--allCPEsOpStateInMG({}): Loading request xml...'.format(mgid))
    with open(NBI.sitepath('/src/XMLReqs/getCPEsByManagedGroup.xml'),'r') as f:
        body = f.read()
    req = ET.fromstring(body)

    report, hasMore, lastIndex = {}, True, 0
    while hasMore:
        req[1][0].find('managedGroupId').text = str(mgid)
        req[1][0].find('lastIndex').text = lastIndex
        if verbose:
            print('--allCPEsOpStateInMG({}): Waiting for server response...'.format(mgid),' '*20)
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
                if verbose:
                    print('--allCPEsOpStateInMG({}): Checking cpe #{}: {}{}'.format(
                            mgid, cpe[0][1].text, state, ' '*10), end='\r')
                report[state] = report.setdefault(state, 0) + 1
    if verbose:
        print('--allCPEsOpStateInMG({}): Process finished'.format(mgid), end=(' '*20)+'\n')
    return report  #dictionary with number of CPEs in each operational state

#Returns a dict of dicts with all the CPEs' operational states for all MGs. Can take very long
def fullOpStateReport(session, verbose=False):
    return {mgid: allCPEsOpStateInMG(session, mgid, verbose) for mgid in NBI.allMGs(verbose=verbose,keepVerbose=verbose)}

#Returns a pretty tabular representation of full opstate report
def prettyFullOpStateReport(session, verbose=False):
    allopstates = fullOpStateReport(session, verbose)
    allstates = sorted(set(st for d in allopstates.values() for st in d))
    maxlen = max(len('Total'), max(len(s) for s in allstates)) + 2
    stringy = ' '*3+'|'+'|'.join(s.center(maxlen) for s in allstates)+'|'+'Total'.center(maxlen)
    headlen = len(stringy)
    for i in sorted(allopstates.keys()):
        stringy += '\n' + '-'*headlen
        states = allopstates[i]
        stringy += '\n' + str(i).center(3) + '|' 
        stringy += '|'.join(str(states.setdefault(s,0)).center(maxlen) for s in allstates)
        stringy += '|' +str(sum(states.values())).center(maxlen)
    return stringy

### Main for debugging purposes ###
if __name__=='__main__':
    import sys
    with requests.Session() as s:
        s.auth=(NBI._username, NBI._password)
        s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': '', 'Connection': 'keep-alive'})

        #mgs = NBI.allMGs(2,True,True)
        #activeCPEs = {i: int(numCPEsOnlineInMG(s,i)) for i in mgs}
        #print('numCPEsOnlineInMG: ', activeCPEs)
        #allCPEs = {i: int(numCPEsInMG(s,i)) for i in mgs}
        #print('numCPEsInMG:', allCPEs)
        #print(allCPEsOpStateInMG(s, 6, True))  
        print(prettyFullOpStateReport(s,'-v' in sys.argv))
         
