from flask import Flask,request

facebook_app= Flask(__name__)


@facebook_app.route("/")
def demo():
    return "Welcome to flask demo"


@facebook_app.route("/post",methods=["POST","GET"])
def login():
    mobile_no =request.json["m.no"]
    password=request.json["password"]
    return f"Login successfully and your mobile_no is {mobile_no},password is {password}"

def create():
    return "hi Sunny"
facebook_app.add_url_rule("/swapna","swa", create)


if __name__ == '__main__':
    facebook_app.run(debug=True)

