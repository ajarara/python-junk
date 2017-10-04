from junk.heaps import heapsort
from random import shuffle


def test_heapsort():
    ordered = list(range(500))
    shuffled = ordered.copy()
    shuffle(shuffled)
    assert [out for out in heapsort(shuffled, ascending=True)] == ordered
