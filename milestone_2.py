import random

def random_word(word_list):
    word = random.choice(word_list)
    return word

def ask_for_guess():
    guess = input("What's your guess?")
    return guess

def check_valid_guess(g):
    if len(g) == 1 and g.isalpha() == True:
        print("Valid guess!")
        return True
    else:
        print("Oops! Your guess needs to be 1 letter")
        return False

