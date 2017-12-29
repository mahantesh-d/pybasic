import json,random,string

a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
print(a)

with open('local_service_requests.json', 'r+', encoding='utf8') as f:
    data = json.load(f)
    data['OrderRef'] = a
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()