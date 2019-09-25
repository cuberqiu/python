import requests
from flask import jsonify, json
# import json
user_info = {"name":"cuberqiu", "password":"123"}
headers = {"Content-Type":"application/json;charset=utf-8"}
# r = requests.post("http://127.0.0.1:5000/users", data=json.dumps(user_info), headers=headers)

r = requests.get("http://127.0.0.1:5000/users/1", headers=headers)

print(r.url)
print(r.headers)
print(type(r.text))
print(r.text)
