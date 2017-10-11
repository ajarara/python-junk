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
