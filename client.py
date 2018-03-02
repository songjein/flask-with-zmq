from flask import Flask
import json
from flask import render_template, request
import zmq
import sys

app = Flask(__name__)

port0 = "9997"
port1 = "9998"

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:%s" % port0)
socket.connect("tcp://localhost:%s" % port1)

@app.route("/")
def index():
    return render_template('index.html') 

@app.route("/search", methods=["POST"])
def search():
    search_term = request.form.get('term') 
    result = [] 

    req_to_server = {
       "term" : search_term 
        }

    # module을 wrapping 하는 zmq서버가 2종류라 가정(blog, news)
    for i in range(2):
        print ("sending request ", json.dumps(req_to_server), "...")
        socket.send (json.dumps(req_to_server).encode())
        # blocked & get the reply
        message = socket.recv()
        result.append(json.loads(message))
        print ("received reply ", i , "[", message, "]")

    #return json.dumps(result)
    return "".join([r["result"] + "</br>" for r in result])

