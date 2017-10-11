

def insertion_sort(arr):
    assert isinstance(arr, list)
    if len(arr) < 2:
        return arr
    for idx, element in enumerate(arr):
        if idx > 0:
            # reversed range is still left inclusive, we want 0.
            for before_idx in range(idx - 1, -1, -1):
                if arr[before_idx] <= element:
                    arr[before_idx + 1] = element
                    break  # everything before this is already sorted.
                arr[before_idx + 1] = arr[before_idx]
