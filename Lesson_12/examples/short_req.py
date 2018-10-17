#!/usr/bin/env python

import sys
from socket import *
from threading import Thread
from time import sleep

HOST = '127.0.0.1'
PORT = 5555
BUFSIZE = 1024

req_count = 0


def reqs_per_sec():
    global req_count
    while True:
        sleep(1)
        print('{} requests/sec'.format(req_count))
        req_count = 0

Thread(target=reqs_per_sec).start()

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        sock.sendall(b'1')
        data = sock.recv(BUFSIZE)
        if not data:
            break
        req_count += 1
