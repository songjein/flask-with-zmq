from flask import Flask
import zmq
import sys

app = Flask(__name__)

port0 = "5556"
port1 = "5556"

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:%s" % port0)
socket.connect("tcp://localhost:%s" % port1)

@app.route("/")
def index():
    result = [] 
    for request in range(1, 10):
        print ("sending request ", request, "...")
        socket.send ("hello".encode())
        # get the reply
        message = socket.recv()
        result.append(message)
        print ("received reply ", request, "[", message, "]")
    return str(result)

