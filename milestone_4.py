import random

import milestone_2
import milestone_3

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = milestone_2.random_word()
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_in_word(self, guess):
        milestone_3.check_in_word(guess)

    def ask_for_input(self):
        guess = milestone_3.ask_for_input()
        if guess in self.list_of_guesses:
            print("You already tied that letter!")
        else:
            self.check_in_word(guess)
            self.list_of_guesses.append(guess)

