#Binary to Decimal converter
#This program converts a binary number to a decimal number
#Created by: Chris
BinaryNumber = input("Enter a binary number: ")
DecimalNumber = 0
for i in range(len(BinaryNumber)):
    DecimalNumber += int(BinaryNumber[i]) * 2 ** (len(BinaryNumber) - i - 1)
print("The decimal number is", DecimalNumber)