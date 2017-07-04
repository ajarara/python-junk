# inspired by yesterday night's meal of a double mcchicken
# 277 is a super-super-super prime. that is:
# 277 is the 59th prime   Super-
# 59 is the 17th prime    Super-
# 17 is the 4th prime     Super!
# 4 is not a prime        :(
# Is 277 peculiarly super prime for its scale or is this common?

from collections import OrderedDict, namedtuple
from math import sqrt
from gödel import next_prime  # remind me to report this.

# are namedtuples just lightweight classes?
prime_metadata = namedtuple('Prime_Metadata', ['index', 'order'])

# why do we use an ordered dictionary? because then we have the
# ability to iterate through our primes, yet access them by their
# 1-based index. These are sorted by order of insertion, not their size
# but we generate (and add) them in that order anyway.
prime_metadata_map = OrderedDict([
    (2, prime_metadata(index=1, order=1)),
    (3, prime_metadata(index=2, order=2)),
])

# here we only care about accessing primes by index, so no need for
# additional memory consumption of a linked list.
# even though OrderedDicts are cool.
index_prime_map = {
    1: 2,
    2: 3,
}


def next_prime(prs):
    '''
    Given a structure like prime_metadata_map, return the next prime,
    along with its prime_metadata.
    '''
    # lifted from gödel.py
    # may it rest in peace.
    prlist = list(prs.keys())
    candidate = prlist[-1] + 2
    cand_sqrt = sqrt(candidate)
    idx = len(prlist) + 1
    idx_prime = False
    while True:
        for pr in prlist:
            if pr == idx:
                idx_prime = True
            if candidate % pr == 0:
                candidate += 2
                idx_prime = False
                break
            # the second check is necessary to check order
            if pr > cand_sqrt and pr >= idx:
                if idx_prime:
                    return (candidate, prime_metadata(idx, 1 + prs[idx].order))
                return (candidate, prime_metadata(idx, 1))


def primes(prs=None):
    if not prs:
        prs = prime_metadata_map
    for prime, meta in prs.items():
        yield prime, meta
    while True:
        prime, meta = next_prime(prs)
        prs[prime] = meta
        yield prime, meta
