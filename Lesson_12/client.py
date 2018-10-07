import socket
import time
import threading


HOST = '127.0.0.1'
PORT = 5005
BUFSIZE = 1024

req_count = 0

def reqs_per_sec():
	global req_count
	while True:
		time.sleep(1)
		print('RPS: {}'.format(req_count))
		req_count = 0

threading.Thread(target=reqs_per_sec).start()

with socket.socket(socket.AF_INET,
			  socket.SOCK_STREAM) as sock:
	sock.connect((HOST, PORT))
	while True:
		sock.sendall((b'1'))
		req_count += 1
		data = sock.recv(BUFSIZE)
		if not data: break
