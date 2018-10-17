#!/usr/bin/env python

from concurrent.futures import ProcessPoolExecutor as Pool
from functools import partial
from socket import *
from threading import Thread

from primes import prime

BUFSIZE = 1024


def prime_handler_pool(pool, conn, addr):
    """ Handler that submits calculation to process pool. """
    with conn:
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            n = int(data)
            fut = pool.submit(prime, n)  # ask pool to perform the calculation
            p = fut.result()             # wait for the result
            conn.sendall(str(p).encode() + b'\n')


def prime_handler(conn, addr):
    with conn:
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            n = int(data)
            p = prime(n)
            conn.sendall(str(p).encode() + b'\n')


def prime_server(host, port, handler=prime_handler):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, int(port)))
        sock.listen()
        print('Listening on {}:{}'.format(host, port))
        while True:
            conn, addr = sock.accept()
            print('Got connection from ' + str(addr))
            Thread(target=handler, args=(conn, addr)).start()


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if args and args[0] == '--pool':
        pool = Pool(4)
        handler=partial(prime_handler_pool, pool)
    else:
        handler=prime_handler
    prime_server('127.0.0.1', 5555, handler=handler)
