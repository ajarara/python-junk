from collections import deque


def filter_d(deq):
    "filters duplicates in a deque, 'in place'"
    accepted = deque()
    while deq:
        key = deq.pop()
        accepted.appendleft(key)
        stage = deque()
        for val in deq:
            if not key == val:
                stage.append(val)
            deq = stage
    return accepted


def glue_deqs(deq1, deq2):
    "What is going on here? This is gross."
    val = deq1.copy()
    val.extend(deq2)
    return val
