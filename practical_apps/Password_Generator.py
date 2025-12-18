#Password Generator
SLetters = "abcdefghijklmnopqrstuvwxyz"
CLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
Symbols = "!@#$%^()_[]`~"

import random

while True:
    SLcount = 0
    CLcount = 0
    Ncount = 0
    Scount = 0
    password = ""
    for i in range(12):
        password += random.choice(SLetters + CLetters + Numbers + Symbols)

    for i in password:
        if i in SLetters:
            SLcount += 1
        elif i in CLetters:
            CLcount += 1
        elif i in Numbers:
            Ncount += 1
        elif i in Symbols:
            Scount += 1
                
    if SLcount > 0 and CLcount > 0 and Ncount > 0 and Scount > 0:
        break

print(f"The password is - {password}")