from flask import Flask,request
from service import *

app = Flask(__name__)

@app.route('/')
def demo1():
    return "Hi SUNNY"


@app.route("/p/<int:num>")
def demo2(num):
   return "The entered number is", str(num)


@app.route("/post1",methods=['POST'])
def post1():
    name=request.json['name']
    id=request.json['id']
    return f'My name is {name} and id is {id}'



@app.route("/vote/<int:a>")
def vote_check(a):
    return vote(a)




'''
@app.route("/loop")
def loop_check():
    list1 = ["hanu","swapna", "sunny",44,546.45]
    for i in list1:
        if type(i) == str:
            return i
        else:
            return str(i)
'''

if __name__ == '__main__':
    app.run()
