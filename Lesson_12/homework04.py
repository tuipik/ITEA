"""
DistributedExecutor - реализация Executor из concurrent.futures,
которая распределяет задачи для выполнения по хостам сети.

DistributedExecutor является одновременно клиентом и сервером,
т.е. позволяет одновременно отправлять задачи на удаленное выполнение
(методы submit, map) и принимать задачи от удаленных хостов (accept).
Это сильно упращает задачу - мы можем подробно не описывать протокол,
так как обе части будут реализованы внутри одной библиотеки.

Для тестирования можете запустить несколько экземпляров на разных портах
локального хоста.

В качестве подсказок по реализации -- список импортов. )
"""

from collections import namedtuple
import concurrent.futures
from concurrent.futures import Executor, Future
from marshal import dumps, loads
from socket import *
import os
from types import FunctionType
from threading import Thread
import fire

HOST = '127.0.0.1'
PORT = 5550
BUFSIZE = 1024



class DistributedExecutor(Executor):
    def __init__(self, addresses=None):
        """
        Аргументы:

        addresses -- iterable, содержащий адреса удаленных хостов (host, port)
        """
        self.addresses = addresses



    def submit(self, *args, **kwargs): #(self, fn, *args, **kwargs):
        """ См. concurrent.futures.Executor.submit() """
        conn = socket()
        conn.connect((HOST, PORT))
        conn.send(dumps(args))
        data = b""
        tmp = conn.recv(BUFSIZE)
        while tmp:
            data += tmp
            tmp = conn.recv(BUFSIZE)
        print(data.decode("utf-8"))
        conn.close()



    def map(self, fn, *iterables, timeout=None, chunksize=1):
        """ См. concurrent.futures.Executor.map() """
        pass

    def shutdown(self, wait=True):
        """ См. concurrent.futures.Executor.shutdown() """
        pass



    def accept(port=5555):
        """
        Реализация серверной, принимающей стороны.
        Запускает сервер (создает слущающий сокет),
        который бесконечно ждет входящих запросов с задачами.

        Аргументы:
        port -- порт для входящих запросов
        """
        sock = socket()
        sock.bind((HOST, PORT))
        sock.listen(10)
        print('Listening {} {}'.format(HOST, PORT))
        conn, addr = sock.accept()
        data = conn.recv(BUFSIZE)
        udata = loads(data)
        print("Data: ",  udata)



if __name__ == '__main__':
    fire.Fire(DistributedExecutor)
#     import sys
#     if sys.argv[1:] == '1':
#         DistributedExecutor.accept()
#     elif sys.argv[1:] == '2':
#         DistributedExecutor.submit()