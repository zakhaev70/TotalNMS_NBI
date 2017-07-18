import http.client
conn = http.client.HTTPConnection("172.19.254.3/ws")
with open('/src/XMLReqs/getCPEpartNumber.xml','r') as f:
	body = f.read()
#print(body)
conn.request("POST", "/cpeService", body)
r1 = conn.getresponse()
print(r1.status, r1.reason)
data = r1.read()
print(data)
with open('resp.xml','w') as w:
	w.write(data)
