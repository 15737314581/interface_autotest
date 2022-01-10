from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


# 1. 获取值

@app.route("/app/case01", methods=["GET"])
def case01():
    flag = request.args.get("flag")
    print(flag)
    return "请求完成"


@app.route("/app/case02", methods=["POST"])
def case02():
    data = request.form.get("flags")
    print(data)
    return {"code": 200, "msg": "success"}


# <> 表示转换 -- 默认类型是STR 字符串
# path: 表示可以使用斜杠
# int 表示正整数
# float 表示浮点数
@app.route("/app/case03/<username>", methods=["GET"])
def case03(username):
    print(type(username))
    print(username)
    return {"code": 200, "msg": "success"}


@app.route("/app/case04", methods=["POST"])
def case04():
    with app.test_request_context('/app/case04', method='POST'):
        assert request.path == '/app/case04', '路由错误'
        assert request.method == 'POST', 'method错误'
    print("4执行")
    return {"code": 200, "msg": "success"}

# 重定向
@app.route("/")
def case05():
    return redirect(url_for("case06"))


@app.route("/hello")
def case06():
    print(1111)
    return render_template("hello.html")


@app.route("/name/<username>")
def case07(username):
    return render_template("hello.html", name=username)


@app.errorhandler(404)
def not_find(error):
    return render_template("error.html"),404




if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(port=8081)