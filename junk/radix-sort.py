
def non_compare(b, idx, low_arr, high_arr):
    if idx < len(b) and b[idx] == "1":
        high_arr.append(b)
    else:
        low_arr.append(b)


# [str] -> [str] :: ordered
def radix_sort(bitstrings):
    "little endian, ascending."
    max_len = 0
    idx = 0
    lows = []
    highs = []

    for b in bitstrings:
        # initialize the maximum length
        max_len = max(max_len, len(b))
        non_compare(b, idx, lows, highs)

    while idx < max_len:
        idx += 1
        bitstrings = lows + highs
        lows = []
        highs = []
        for b in bitstrings:
            non_compare(b, idx, lows, highs)

    return bitstrings
