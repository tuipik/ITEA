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
from concurrent.futures import Executor, Future
from marshal import dumps, loads
from socket import *
from types import FunctionType
from threading import Thread


class DistributedExecutor(Executor):
    def __init__(self, addresses=None):
        """
        Аргументы:

        addresses -- iterable, содержащий адреса удаленных хостов (host, port)
        """
        self.addresses = addresses

    def submit(self, fn, *args, **kwargs):
        """ См. concurrent.futures.Executor.submit() """
        pass

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
        pass
