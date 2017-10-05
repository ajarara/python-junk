from collections import deque


def merge_q(left, right):
    out = []
    ql = deque(left)
    qr = deque(right)
    while ql and qr:
        if ql[0] <= qr[0]:
            out.append(ql.popleft())
        else:
            out.append(qr.popleft())
    out.extend(ql or qr)
    return out


def merge_sort_q(arr):
    if len(arr) <= 1:
        return arr
    bound = len(arr) // 2
    left = arr[:bound]
    right = arr[bound:]

    return merge_q(
        merge_sort_q(left),
        merge_sort_q(right))

# huh running this with a large shuffled array didn't cause a large amount of memory issues. are left and right views?
# or is it doing some pool allocation? I don't think python does that.
# it did take a LONG time though. 4 minutes of compute time so far.

# I ended up interrupting this. It works correctly it is just hideously slow.

# heapsort in place was a LOT faster. I gotta investigate this.

# this has a lot of ramifications. Maybe I should ask RC, specifically Jayant.
# maybe it has to do with malloc?
# who knows.

def merge(left, right):
    out = []
    left_idx, right_idx = (0, 0)
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            out.append(left[left_idx])
            left_idx += 1
        else:
            out.append(right[right_idx])
            right_idx += 1
    # now get whatever is left from each
    if left_idx >= len(left):
        out.extend(right[:right_idx])
    else:
        out.extend(left[:left_idx])
    return out

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    bound = len(arr) // 2
    left = arr[:bound]
    right = arr[bound:]

    return merge(
        merge_sort(left),
        merge_sort(right))


#         3773202 function calls (3573204 primitive calls) in 1.012 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    1.012    1.012 <string>:1(<module>)
# 199999/1    0.179    0.000    1.010    1.010 merge.py:17(merge_sort_q)
#    99999    0.642    0.000    0.814    0.000 merge.py:4(merge_q)
#        1    0.000    0.000    1.012    1.012 {built-in method builtins.exec}
#   299998    0.017    0.000    0.017    0.000 {built-in method builtins.len}
#  1536602    0.090    0.000    0.090    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    99999    0.014    0.000    0.014    0.000 {method 'extend' of 'list' objects}
#  1536602    0.068    0.000    0.068    0.000 {method 'popleft' of 'collections.deque' objects}


