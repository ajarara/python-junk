# Python-Junk
A collection of oddities concerning python3.

## Instead only try to realize the Truth... there is no list



``` python
def square(num):
    return num ** 2
    
results = map(square, range(5))

# python3 specific

type(results)
# <class 'map'>

list(results)
# [0, 1, 4, 9, 16]

list(results)
# []

```

Source: http://stackoverflow.com/a/19117067

python3's map returns a map object, which is pretty much an
iterable. Contrast this with python2.7's map, which returns a list
immediately (that is, ```list(results) == results```)

This whole page is filled with some great info, and reveals some
startling truths about python. Consider also the answer
(**fixed in python3**) proposed by Mehrdad here:
http://stackoverflow.com/a/13483314 (same page), where x is silently
overwritten in the code run after the comprehension in the first
part. That is, list comprehensions do not introduce new scope.


## memory consumption of dicts

Back in college I used to play around with Java. I had this weird affinity with ArrayList, I never really wanted to use Array because I generally was doing weird stuff where I did not know the length of my Array.

What I didn't understand was that ArrayList was clearly backed by Arrays, but gave me some conveniences: It would start with a small size allocated in memory, and when it ran out, it would copy the array over, allocating twice the space for it. This caused some insertion events to take long, in fact copying arrays is an O(N) operation, but since it occurs every N inserts, insertion is effectively constant.

This is pretty much the case with python3 dictionaries.

Code from dict.py, hosted in this repo
``` python
import sys


def supersize_me(num, interval):
    "docstring"
    bag_of_nums = dict()
    for i in range(num):
        bag_of_nums[i] = 1
        if i % interval == 0:
            print(i, ":", sys.getsizeof(bag_of_nums))
            
supersize_me(100, 10)
# 0 : 288
# 10 : 480
# 20 : 864
# 30 : 1632
# 40 : 1632
# 50 : 3168
# 60 : 3168
# 70 : 3168
# 80 : 3168
# 90 : 6240
```

Alternatively:
``` python
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

supersize_you(10 ** 6)
# 5 : 480
# 11 : 864
# 21 : 1632
# 43 : 3168
# 85 : 6240
# 171 : 12384
# 341 : 24672
# 683 : 49248
# 1365 : 98400
# 2731 : 196704
# 5461 : 393312
# 10923 : 786528
# 21845 : 1572960
# 43691 : 3145824
# 87381 : 6291552
# 174763 : 12583008
# 349525 : 25165920
# 699051 : 50331744
```

For a very nice talk by Raymond Hettinger: https://www.youtube.com/watch?v=p33CVV29OG8
# For loops

