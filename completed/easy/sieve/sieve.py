def sieve(n):
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [prime for prime, checked in enumerate(primes) if checked]
