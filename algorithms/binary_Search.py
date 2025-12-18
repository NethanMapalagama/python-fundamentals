# Binary Search

def binary_search(item, Arry):
    if len(Arry) == 0:
        print("Item is NOT found")
        return
    mid = len(Arry) // 2
    if item == Arry[mid]:
        print("Item Found")
        return
    elif item > Arry[mid]:
        return binary_search(item, Arry[mid+1:])
    else:
        return binary_search(item, Arry[:mid])
