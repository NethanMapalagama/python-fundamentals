import random
import pyfiglet
from gallowstates import GALLOW_STATES

# Random word Finder
def random_finder():
    word_list = r"python/Hangman Game/words.txt"
    words = open(word_list,"r")
    word_lines = []
    for word in words:
        cleaned = word.strip()
        word_lines.append(cleaned)
    random_word = random.choice(word_lines)
    words.close()
    return random_word


# Welcome Message
def print_welcome():
    text = pyfiglet.figlet_format("Hangman!", font="big")
    print(f"{text:^39}")
    print("Be careful with the letters you choose!")
    print("")
    print("")

# Start the game
def game():
    the_word = random_finder()
    len_word = len(the_word)
    word_array = list(the_word.lower())
    blank_word = ['_' for i in range(len_word)]
    print("")
    print(f"Your word is {''.join(blank_word)}\n{len_word} letters long. You got 7 strikes")

    count = 0
    used_letters = []
    while True:
        print("")
        if len(used_letters) > 0:
            print("Used letters: " + ", ".join(used_letters))
            print("")                  
        letter = input("Enter a letter: ").lower()
        if letter in used_letters:
            print("You already used that letter. Try another one.")
            continue
        else:
            used_letters.append(letter)
        if letter in word_array:
            positions = [i for i, ch in enumerate(word_array) if ch == letter]
            for i in positions:
                blank_word[i] = letter
            print("".join(blank_word))
        else:
            count += 1
            if count != 6:
                print(f"Oops, not in the word, {count} strike")
            else:
                print(f"Oops, not in the word, last strike")
            print(GALLOW_STATES[count-1])
            if count == 7:
                gameover_text = pyfiglet.figlet_format("Game Over", font="big")
                print(f"{gameover_text:^39}")
                print(f"The word was - {the_word}")
                print("")
                break
        if blank_word == word_array:
            victory_text = pyfiglet.figlet_format("Victory", font="big")
            print(f"{victory_text:^39}")
            break

def Hangman():
    print_welcome()
    while True:
        user_input = input('Type "start" to start the game\nType "end" to end the game\n: ').lower()
        if user_input == "start":
            game()
        elif user_input == "end":
            break
        else:
            print("Enter a valid input!")


Hangman()