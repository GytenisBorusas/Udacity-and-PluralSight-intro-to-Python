'''
    File name: wordgames.py
    Author: Gytenis Borusas
    Date created: 11/27/2016
    Date last modified: 12/06/2016
    Python Version: 3.5

    A word guessing game.
'''


import random


# Creates function for words list("words") and randomly selected
#  one word("word") from the list.
def get_random_word():
    words = ["pizza", "cheese", "apples", "nuts", "tomatoes", "turkey"]
    word = words[random.randint(0,len(words)-1)]
    return word

#
def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

# Accepts inputs from the screen.
def get_guess():
    print("Guess the letter: ")
    return input()

# Created function which checks if the input letter is same
# as one of the word letters.
def process_letter(letter, secret_word, blanked_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter
    return result

# Keeps count of the strikes and shows them with "X"
# denotation on the screen
def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X ", end="")
    print("")

# Game function and initialized variables "strikes", "max_strikes",
# Also initializes new local variable "words" and "blanked_words".
def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    word = get_random_word()
    blanked_word = list( "_" * len(word))

# Defines how the game works, how the inputs are checked against
# the randomly selected word and false counts counted.
    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

# Prints out the end of the game result.
    if strikes >= max_strikes:
        print("You lost")
    else:
        print("You are the Winner")


# Initializes the game function and prints output when the game is over.
print("Game started")
play_word_game()
print("Game over")