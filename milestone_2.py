import random

word_list = ["Apple", "Kiwi", "Banana", "Watermelon", "Mango"]
print(word_list)

def random_word():
    word = random.choice(word_list)
    print(word)
    return word

def ask_for_guess():
    guess = input("What's your guess?")
    return guess

def check_guess(g):
    if len(g) == 1 and g.isalpha() == True:
        print("Good guess!")
        return True
    else:
        print("Oops! Your guess needs to be 1 letter")
        return False
