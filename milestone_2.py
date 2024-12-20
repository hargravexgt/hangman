import random

word_list = ['mango', 'pineapple', 'blueberry', 'orange', 'watermelon']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Choose a letter:")

if guess.isalpha() and len(guess)== 1:
    print("Good guess!")
else:
    print("Oops that is not a valid input!")