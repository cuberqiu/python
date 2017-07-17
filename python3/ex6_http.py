from urllib import request, parse
import requests

payload = {'key1': 1, 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

print(type(r.json()),r.json())

data = r.json()

# print(text['args'])


print(type(data['args']['key1']),data['args']['key1'])