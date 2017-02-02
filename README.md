# Python-Junk
-------------
A collection of oddities concerning python3.

## Instead only try to realize the Truth... there is no list



``` python
def square(num):
    return num ** 2
    
results = map(square, range(5))

list(results)
# [0, 1, 4, 9, 16]

list(results)
# []

```

Source: http://stackoverflow.com/a/19117067

python3's map returns a map object, which is pretty much an iterable. Contrast this with python2.7's map, which returns a list immediately (that is, ```list(results) == results```)

This whole page is filled with some great info, and reveals some startling truths about python. Consider also the answer proposed by Mehrdad here: http://stackoverflow.com/a/13483314 , where x is silently overwritten in the code run after the comprehension in the first part. That is, list comprehensions do not introduce new scope.

Which is interesting. Of course you need to inherit the environment of the comprehension to do anything useful, but binding should specifically 

