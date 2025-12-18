def total(myArray):
    if len(myArray) == 0:
        result = 0
    else:
        result = myArray[0] + total(myArray[1:len(myArray)])
    return result

myArray = [1,2,3,5,6,7,8,9]

print(total(myArray))

def iterativeTotal(myArray):
    total = 0
    for num in myArray:
        total += num
    return total

def menu():
    while True:
        choice = int(input("Enter the choice of the programme\n 0. Exit\n 1. total()\n 2. iterativeTotal()\nEnter: "))
        match choice:
            case 0:
                break
            case 1:
                result = total(myArray)
                print("total() result = ",result)
            case 2:
                result = iterativeTotal(myArray)
                print("iterativeTotal() = ",result)
        
menu()