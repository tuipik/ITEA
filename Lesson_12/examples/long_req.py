#!/usr/bin/env python

import sys
import time
from socket import *
from threading import Thread


HOST = '127.0.0.1'
PORT = 5555
BUFSIZE = 1024


with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        start = time.time()
        sock.sendall(b'30000')
        data = sock.recv(BUFSIZE)
        if not data:
            break
        end = time.time()
        print(round(end - start, 3))
