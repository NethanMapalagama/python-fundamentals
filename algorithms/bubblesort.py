items = [1, 5, 7, 6, 4, 3, 8, 9, 2, 0]  # items: ARRAY OF INTEGER

def bubbleSort():
    global items
    i = 0  # i: INTEGER
    swapped = True  # swapped: BOOLEAN
    # (1) outer loop for every "pass"
    #     ... if nothing was swapped by the end of a pass, the array is already sorted
    while i < len(items) - 1 and swapped == True:
        swapped = False
        # (2) inner loop for every "comparision"
        for j in range(len(items)-i-1):  # j: INTEGER
             # (3) check if the current item is greater than the next item
            if items[j] > items[j+1]:
                # (4) if true, swap the items
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        i += 1

bubbleSort()
print(items)  # OUTPUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]