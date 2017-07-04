# inspired by yesterday night's meal of a double mcchicken
# 277 is a super-super-super prime. that is:
# 277 is the 59th prime   Super-
# 59 is the 17th prime    Super-
# 17 is the 4th prime     Super!
# 4 is not a prime        :(
# Is 277 peculiarly super prime for its scale or is this common?

from collections import OrderedDict, namedtuple, deque
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


def next_prime(prs):
    '''
    Given a structure like prime_metadata_map, return the next prime,
    along with its prime_metadata.
    '''
    # lifted from gödel.py
    # may it rest in peace.
    last = next(reversed(prs))
    candidate = last + 2
    cand_sqrt = sqrt(candidate)
    idx = prs[last].index + 1
    idx_prime = idx in prs
    while True:
        prlist = iter(prs)
        for pr in prlist:
            # print("pr: {}, candidate: {}".format(pr, candidate))
            if candidate % pr == 0:
                candidate += 2
                cand_sqrt = sqrt(candidate)
                break
            if pr > cand_sqrt:
                # print(
                #     "accepted candidate: {}, since {} > {}".format(candidate, pr, cand_sqrt))
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


def primes_until(top, prs=None):
    # sieve implementation. any prs are assumed to be prime already.
    if prs is None:
        prs = prime_metadata_map
        # start from where we left off
        last = next(reversed(prs))
    elif isinstance(prs, OrderedDict) and prs:
        last = next(reversed(prs))
    else:
        raise TypeError("prs must be an nonempty OrderedDict or None")
    if last > top:
        # already calculated, just return a slice.
        return OrderedDict(
            [(prime, meta) for prime, meta in prs.items() if prime <= top]
        )
        
    raw = _sieve(top, prs, last)
    # now we need to annotate these new primes, append them to the
    # prime_metadata_map and return the prime_metadata_map
    _annotate_and_add(prs, raw)
    return prs


def _sieve(top, prs, last):
    to_be_sieved = deque(range(last + 1, top + 1))
    for pr in prs:
        sieved = deque()
        while to_be_sieved:
            candidate = to_be_sieved.popleft()
            if candidate % pr != 0:
                sieved.append(candidate)
        to_be_sieved = sieved
    # now we turn the sieve on itself. If there was no prime list then
    # this is the standard sieve algo
    accepted = deque()
    while to_be_sieved:
        prime = to_be_sieved.popleft()
        accepted.append(prime)
        sieved = deque()
        for candidate in to_be_sieved:
            if candidate % prime != 0:
                sieved.append(candidate)
        to_be_sieved = sieved
    return accepted


# destructive operation on prs
def _annotate_and_add(prs, raw):
    for prime in raw:
        idx = next(reversed(prs.values())).index + 1
        idx_prime = idx in prs
        if idx_prime:
            prs[prime] = prime_metadata(idx, 1 + prs[idx].order)
        else:
            prs[prime] = prime_metadata(idx, 1)

