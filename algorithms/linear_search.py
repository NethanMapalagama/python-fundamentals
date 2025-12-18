def linear_search(arr, target):

    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1

def linear_search_r(arr,target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    res = linear_search_r(arr[1:], target)
    return res + 1 if res != -1 else -1
