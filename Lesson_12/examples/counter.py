from threading import Lock, Thread


class NaiveCounter():
    def __init__(self):
        self.count = 0

    def incr(self):
        self.count += 1


class Counter():
    def __init__(self):
        self.count = 0
        self._lock = Lock()

    def incr(self):
        with self._lock:
            self.count += 1


def task(n, counter):
    for _ in range(n):
        counter.incr()


def test(counter_type):
    counter = counter_type()
    def _test(nops=100000, nthreads=5):
        threads = [Thread(target=task, args=(nops, counter))
                   for _ in range(nthreads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        print(nops*nthreads, counter.count)
    return _test


from timeit import timeit

print(timeit(test(NaiveCounter), number=1))
print(timeit(test(Counter), number=1))
