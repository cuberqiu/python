from flask import Flask, request, url_for, jsonify, json, Response

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'hello world\n'


@app.route('/register', methods=['POST'])
def register():

    r_kwargs = request.get_json(force=True)
    #
    print(type(r_kwargs))
    print(r_kwargs)

    rtn_msg = {"1":"cuber", "2":"piper"}
    return jsonify(r_kwargs)


@app.route('/form', methods=['POST'])
def form():
    userName = request.form
    print(type(userName))
    print(dict(userName))
    for key in userName:
        print(type(key))
        print(type(userName[key]))
        print(key, " ", userName[key])
    return jsonify(userName)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()