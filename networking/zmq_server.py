import zmq

host = '127.0.0.1'
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)