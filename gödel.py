from math import sqrt
import operator


# First we need a list of primes. This is a naive algo, but I'm not
# really interested in efficiency beyond the first 256 primes as we
# all know english best-lish

# using a global cache so that we can generate by length and by maximum
# yes, this is ugly. yes, this probably belongs in a redis store
# unfortunately I don't have enough caffeine to care about ugly.
_cache=[2,3]

def gen_primes(n):
    ''' generate the first n primes. return them. '''
    if len(_cache) > n:
        return _cache[n - 1:].copy() # so we don't deal with any shenanigans.

    while len(_cache) < n:
        _cache.append(next_prime(_cache))

    return _cache[:n].copy()


def gen_primes_until(maximum):
    ''' generate prime until maximum. For now, returns the whole prime list'''
    while True:
        candidate = next_prime(_cache)
        if candidate > maximum:
            return _cache.copy()
        else:
            _cache.append(candidate)


def next_prime(prlst):
    ''' given a list of primes, return the next one. '''
    # make sure maximum prime is last one.
    assert sorted(prlst) == prlst

    # make sure first two elements are 2, 3.
    assert prlst[:2] == [2, 3]

    # start from end, increment by 2
    start = prlst[-1] + 2
    while True:
        for pr in prlst:
            if start % pr == 0:  # if a prime divides our candidate
                start += 2  # find a new candidate!
                break  # break out of the for, no need to continue
            if pr ** 2 > start:  # we found a prime!
                return start
    

# now that we can generate a list of primes, we have our bijection: the gödel numbering!
def gödelize(string):
    pr = gen_primes(len(string))
    seq = [pr[index] ** ord(string[index]) for index in range(len(string))]
    result = 1
    for num in seq:
        result = result * num
    return result


# this wouldn't be a bijection if we couldn't formulate the inverse!
# def rev_gödelize(number):
#     ''' infinite loop '''
#     assert number > 0 and (number) == int
    
#     # cowboy coding best coding
#     exp = []
#     i = 0
    
#     while number != 1:  # every integer has a prime factorization
#         # avoiding an index error:
#         if i > (len(_cache) -1):
#             pass
#         while number % prime[i] == 0
            
def bump_cache():
    _cache.append(next_prime(_cache))

# -------------------- sane program termination --------------------

def op_btarray(b1, b2, op):
    return bytes(map(lambda bit1, bit2 : op(bit1, bit2), b1, b2))

# likely possible to extend this to infinitely many args.
def xor_str(s1, s2, op=operator.xor, en='utf-8'):
    ''' returns result of mapping op of string in given encoding '''
    b1 = bytes(s1, en)
    b2 = bytes(s2, en)
    return op_btarray(b1, b2, op).decode(en)

# utf-8 defines "A" as 65, "z" as 122. We're gonna try if any of these map to some real letter.

BOTTOM="A"
TOP="z"
def valid_ops(op):
    ''' Op should be symmetric, that is, a ^ b == b ^ a for all a,b, in the domain of ^ '''
    low = ord(BOTTOM)
    high = ord(TOP)
    for i in (range(low, high + 1)):  # include top.
        j = i  # set j to 0 if the op is not symmetric
        while j < high + 1:
            res = op(i, j)
            if low < res < high:
                print("{} applied to {}, {} yields valid value: {}\n".format(repr(op), i, j, res))
            j += 1
                
        
    
