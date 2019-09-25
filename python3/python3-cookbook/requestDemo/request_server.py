import requests
import json
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/')
def api_hello():
    return "hello"


@app.route('/messages', methods=['POST'])
def api_message():
    # return "JSON Message: "+ json.dumps(request.json)+"\n"
    r_kwargs = request.get_json(force=True)
    #
    print(type(r_kwargs))

    url = "http://10.241.106.212:80/graphs/getEdges"

    headers = {"Content-Type": "application/json;charset=utf-8"}

    r = requests.post(url, data=json.dumps(r_kwargs), headers=headers)

    d = json.loads(r.text)

    print(d)
    # print(r_kwargs)
    return jsonify(d)



if __name__ == '__main__':
    app.run()
