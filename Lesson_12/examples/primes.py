from itertools import count, islice

def primes():
    yield 2
    for n in count(3, 2):
        for d in count(3, 2):
            if d > n ** 0.5:
                yield n
                break
            if n % d == 0:
                break


def prime(n):
    return next(islice(primes(), n, None))
