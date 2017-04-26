import sys
from collections import defaultdict

def supersize_me(num, interval):
    "docstring"
    bag_of_nums = dict()
    for i in range(num):
        bag_of_nums[i] = 1
        if i % interval == 0:
            print(i, ":", sys.getsizeof(bag_of_nums))


def supersize_you(num):
    "docstring"
    bag_of_nums = dict()
    old = sys.getsizeof(bag_of_nums)

    for i in range(num):
        bag_of_nums[i] = 1
        size = sys.getsizeof(bag_of_nums)
        if size != old:
            print(i, ":", size)
            old = size


def chardict(somestr):
    """ given a string, return a profile of the characters in it. make
    no assumptions about its encoding """
    count = {}
    for char in somestr:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def hashchr():
    letter_hashes = [hash(chr(ind)) for ind in range(64, 90)]
    
    assert sorted(letter_hashes) == letter_hashes  # preserves ordering
    
    for i in range(len(letter_hashes) - 1):
        # also is semi-equally spaced. weird.
        print("diff: {}".format(letter_hashes[i + 1] - letter_hashes[i]))


