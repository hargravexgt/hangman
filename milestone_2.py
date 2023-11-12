import random

def random_word(word_list):
    """This function randomly selects a word from a word list."""
    word = random.choice(word_list)
    return word

def ask_for_guess():
    "This function asks for a guess."
    guess = input("What's your guess?")
    return guess

def check_valid_guess(g):
    "This function checks that the guess is a single letter, and tells us whether it is or not."
    if len(g) == 1 and g.isalpha() == True:
        print("Valid guess!")
        return True
    else:
        print("Oops! Your guess needs to be 1 letter")
        return False

