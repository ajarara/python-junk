from collections import defaultdict

a = defaultdict([])
print(repr(a[5]))
a[5] = 100
b = defaultdict([])
print(repr(b[5]))
