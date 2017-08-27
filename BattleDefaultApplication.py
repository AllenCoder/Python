import urllib

from bottle import Bottle, run, request,response, static_file
import json

app = Bottle()


@app.route("/hello")
def hello():
    return "Hello World"


@app.route("/world")
def word():
    return "world"


@app.route("/activities", method='POST')
def activities():
    body = request.body.read()
    # parsedBody = urllib.unquote(body).decode('utf8')
    print("收到上传请求", body)
    from json import dumps
    rv = {"code": 1, "message": "Test Item 1"}
    response.content_type = 'application/json'

    return  dumps(rv)


@app.route('/login')
def login():
    print("打印", request.body)
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


def check_login(username, password):
    print(username, password)
    return True


@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    header = request.headers.get("header")
    cookies = request.cookies.get('counter', "0")
    form_id = request.query.id
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


# 静态文件
@app.route('/file')
def file():
    return static_file("170717007.xml", root="")


# 下载文件
@app.route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='', download=filename)


run(app, host="192.168.1.102", port=8089)

# run(app, host="localhost", port=8089)
