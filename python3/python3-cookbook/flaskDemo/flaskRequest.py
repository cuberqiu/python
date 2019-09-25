from flask import Flask, request, url_for, jsonify, json, Response
from functools import wraps

"""
curl 指令参考：
-X    指定HTTP请求方法，例如POST，GET
-H    指定请求头，例如Content-Type:application/json
-d    指定请求数据
--data-binary  指定发送的文件
-i    显示响应头部信息
-u    指定认证用户名与密码
-     输出请求头部信息
"""

app = Flask(__name__)

@app.route('/')
def api_root():
    return "mac Welcome\n"


@app.route('/articles')
def apt_articles():
    return 'List of ' + url_for('apt_articles') + "\n"


@app.route('/articles/<articleid>')
def api_articleid(articleid):
    return 'You are reading ' + articleid + "\n"


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return "Hello cuberqiu\n"


@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"
    elif request.method == 'POST':
        return "ECHO: POST\n"
    elif request.method == "PATCH":
        return "ECHO: PATCH\n"
    elif request.method == "PUT":
        return "ECHO: PUT\n"
    elif request.method == "DELETE":
        return "ECHO: DELETE"


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: "+request.data+"\n"
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: "+ json.dumps(request.json)+"\n"
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./file/binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"+"\n"

    else:
        return "415 Unsupported Media Type !"+'\n'


@app.route('/rhello', methods=['GET'])
def api_rhello():
    data = {
        'hello': "cuberqiu",
        'number': 3
    }

    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp


# 错误处理
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':"Not Found: "+ request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {"1": "cuberqiu", "2":"andy", "3":"piper"}
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()


# 认证
def check_auth(username, password):
    return username=='admin' and password=='secret1'


def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp


def requeres_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route('/secrets')
@requeres_auth
def api_shello():
    return "Shhh this is top secret spy stuff!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)