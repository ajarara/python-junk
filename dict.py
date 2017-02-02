import sys


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
