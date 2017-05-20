# inspired by yesterday night's meal of a double mcchicken
# 277 is a super-super-super prime. that is:
# 277 is the 59th prime   Super-
# 59 is the 17th prime    Super-
# 17 is the 4th prime     Super!
# 4 is not a prime        :(
# Is 277 peculiarly super prime for its scale or is this common?

# first we import our prime mechanisms

from gödel import gen_primes, gen_primes_until, next_prime

# given a prime, find its index in the prime list.
def index_prime(prime):
    ''' given a prime, find its index in the prime list '''
    primelist = gen_primes_until(prime)  # this does 

    # admittedly this is hacky
    try:
        assert next_prime(primelist) == prime

        
        return len(primelist) + 1 
    except AssertionError:
        print("{} is not prime!".format(prime))








