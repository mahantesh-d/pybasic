import requests,json,random,string,time
from datetime import datetime

print("Starting script")

url = 'http://10.252.169.12:7788/v1/customers/customerOrder/localServiceRequests.json'
headers = {'Authorization' : '(anything)', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

with open('local_service_requests.json', 'r+', encoding='utf8') as f:
	g = f.read()
	data = json.loads(g)
	f.close()
	
for x in range(200):
	print("Starting loop")
	tmp = data
	tmp['OrderRef'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
	r = requests.post(url, data=json.dumps(tmp), headers=headers)
	k = "Time ", str(r.elapsed), ", Status Code ", r.status_code, " Reason ", r.reason, " Body "
	print(k)
	r.close()
	time.sleep(1)