unsorted_array = [64, 34, 25, 12, 22, 11, 90]

def insertionsort(u_array: list) -> list:
    
    for i in range(1,len(u_array)):
        value = u_array[i]
        j = i - 1
        while j >= 0 and value < u_array[j]:
            u_array[j+1] = u_array[j]
            j-=1
        u_array[j+1] = value

    return u_array


sorted_array = insertionsort(unsorted_array)
print(sorted_array)