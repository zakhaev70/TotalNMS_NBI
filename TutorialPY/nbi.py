import requests

host = 'http://172.19.254.3/ws'

with requests.Session() as s:
    s.auth=('admin','manager')
    #s.verify = False  # only needed if https with no SSL certificate
    s.headers.update({'Content-Type': 'text/xml;charset=UTF-8', 
            'SOAPAction': '', 'Connection': 'keep-alive'})

    with open('../XMLReqs/getCPEsByManagedGroup.xml','r') as f:
        body = f.read()

    r = s.post(host+'/cpeService', data=body)
    print(r)  # response object
    print('-'*60)
    print(r.text)  # response body

