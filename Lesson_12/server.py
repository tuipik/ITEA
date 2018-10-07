import socket
import threading
from threading import Thread
from itertools import count, islice
from concurrent.futures import ThreadPoolExecutor


HOST = '127.0.0.1'
BUFSIZE = 1024


def primes():
	yield 2
	for n in count(3, 2):
		for d in count(3, 2):
			if d > n ** 0.5:
				yield n
				break
			if n % d == 0:
				break

pool = ThreadPoolExecutor(5)
def prime(n):
	return next(islice(primes(), n, None))



def handler(conn, addr):
	with conn:
		while True:
			# print('Gotta connection from ' + str(addr))
			data = conn.recv(BUFSIZE)
			if not data:
				print(data.decode())
				break
			data = data.decode().rstrip()
			n = int(data)
			p = prime(n)
			future = pool.submit(prime, p)
			result = future.result()
			conn.sendall(str(result).encode())


def echo_serv(port):
	# print('Main thread ', str(threading.get_ident()))

	with socket.socket(socket.AF_INET,
					   socket.SOCK_STREAM) as sock:
		sock.bind((HOST, port))
		sock.listen(5)
		print('Listening {} {}'.format(HOST, port))
		while True:
			conn, addr = sock.accept()
			# print('Gotta connection from ' + str(addr))
			# handler(conn, addr)
			t = Thread(target=handler, args=(conn, addr))
			t.start()


if __name__ == '__main__':
	import sys
	args = sys.argv[1:]
	assert args, 'Usage: server PORT'
	echo_serv(int(args[0]))
