import random

word_list = ['mango', 'pineapple', 'blueberry', 'orange', 'watermelon']

def get_random_word_from_list(list):
    return random.choice(list)

word = get_random_word_from_list(word_list)

def check_if_guess_valid(guess):
    if guess.isalpha() and len(guess)== 1:
        print("Good guess!")
    else:
        print("Oops that is not a valid input!")

if __name__ == "__main__":
    print(word_list)
    print(word)
    guess = input("Choose a letter:")
    check_if_guess_valid(guess)
