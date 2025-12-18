#Guess the Number!

#Game Rules!
#The computer picks a random number between 1 and 100.
#The player keeps guessing until they find the correct number.
#The game provides hints like "Too high!" or "Too low!" after each guess.
#The game ends when the player guesses correctly.

def PickNumber():
    import random
    return random.randint(1,100)

def GuessNum():
    PickedNum=PickNumber()
    Guess = int(input("Enter a number between 1-100: "))

    while Guess>100 or Guess<1:
        Guess = int(input("Enter a number between 1-100: "))
    i=1    
    while PickedNum != Guess:
        if Guess>PickedNum:
            Guess=int(input(f"Guess is too high,try again {i}: "))
        else:
            Guess=int(input(f"Guess is too low,try again ({i}): "))
        i=i+1

    print(f"You Succesfully guessed the number {PickedNum}")


GuessNum()    