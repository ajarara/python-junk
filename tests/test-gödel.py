# not actual  tests. Not sane tests. Tear downs embedded in them. Sadness abounds! 

def prime_test():
    primes = gen_primes(10)
    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[2] == 5
    assert primes[3] == 7
    # it goes up to 11
    assert primes[4] == 11

def _tear_down_prime_test2():
    _cache = [2, 3]
    primes = gen_primes_until(28)
    assert primes[-1] == 29
    

def _next_prime_test():
    assert _next_prime([2,3]) == 5
    assert _next_prime([2,3,5]) == 7
