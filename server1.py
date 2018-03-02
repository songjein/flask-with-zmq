import zmq
import time
import sys
import json

port = "5556" # default
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    # wait for next request from client
    message = socket.recv()
    print ("Received request: ", message)
    term = json.loads(message)["term"]
    time.sleep(1)
    res_to_client = {
       "result" : "블로그 검색 결과 about %s from %s" % (term, port)
        }
    socket.send(json.dumps(res_to_client).encode())

