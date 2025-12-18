# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

stack = []
def countdown(n):
    if n != 0 and n <= 5 :
        stack.append(n)
        countdown(n-1)
    

def reverse_sender(text):
    if len(text) <= 1:
        return text
    return reverse_sender(text[1:])+text[0]

# ABCD
# BCD
# CD 
# D      
# D + [C]D 
# DC + [B]CD 
# DCB + [A]BCD
    
print(reverse_sender("ABCD"))

