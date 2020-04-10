from flask import Flask, request
from json import dumps

APP = Flask(__name__)
APP.debug = True

userList = {}

@APP.route('/user/create', methods=['POST'])
def create():
    global userList
    password = request.form.get('password')
    secret = request.form.get('secret')
    d = {
        'password': password,
        'secret': secret,
        'token': password + '12345abcd'
    }
    userList.update(d)
    return dumps({'token': userList['token']})

@APP.route('/user/connect', methods=['PUT'])
def connect():
    global userList
    password = request.form.get('password')
    if password == userList['password']:
        return dumps({'token': userList['token']})
    else:
        return "incorrect password"

@APP.route('/user/secret', methods=['GET'])
def secrete():
    global userList
    token = request.args.get('token')
    if token == userList['token']:
        return dumps({'secret': userList['secret']})
    else:
        return "incorrect token"


if __name__ == '__main__':
    APP.run()
