import flask
import json

from flask import request

"""
flask web框架，通过flask提供的装饰器@selrver.route()将普通函数转换为服务 

"""

server = flask.Flask(__name__)

@server.route('/login',methods=['get','post'])
def login():

    username = request.values.get("name")
    pwd = request.values.get('pwd')

    if username and pwd:
        if username == "xiaoming" and pwd == "123456":
            result = {"code":200,"message":"登陆成功！"}
            # return json.dumps(result,ensure_ascii=False)

        else:
            result = {"code":-1,"message":"账号或者密码错误"}

    else:
        result = {
            "code":10001,
            "message":"参数不能为空"
        }

    return json.dumps(result,ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True,host="127.0.0.1",port="8888")