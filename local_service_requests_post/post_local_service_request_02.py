import requests,json,random,string,time
from datetime import datetime

for x in range(4000):
    a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
    #print(a)

    with open('local_service_requests2.json', 'r+', encoding='utf8') as f:
        data = json.load(f)
        data['OrderRef'] = a
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    url = 'http://10.252.169.12:7788/v1/customers/customerOrder/localServiceRequests.json'

    headers = {'Authorization' : '(anything)', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    r = requests.post(url, data=open('local_service_requests2.json', 'rb'), headers=headers)
    print("Time ",r.elapsed)
    print('Status Code: ',r.status_code)
    print(r.reason)
    r.close()
    with open('out9.txt', 'a') as f:
        f.write(str(datetime.now()) + "\t Status Code: " + str(r.status_code) + "\t Response Time: " + str(r.elapsed) + "\n")
        f.close()
#time.sleep(0.03)