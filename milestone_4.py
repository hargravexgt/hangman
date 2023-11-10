import random

import milestone_2
import milestone_3

word_list = ["Apple", "Kiwi", "Banana", "Watermelon", "Mango"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = milestone_2.random_word(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_in_word(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess: {guess} is in the word")
            for letter in self.word:
                if letter == guess:
                    idx = self.word.index(guess)
                    self.word_guessed[idx] = guess
        else:
            print(f"Sorry, {guess} not in the word. Try again!")


    def ask_for_input(self):
        guess = milestone_3.ask_for_input()
        print(f"Guess: {guess}, Word: {self.word}")
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_in_word(guess)
            self.num_letters =+ -1
            self.list_of_guesses.append(guess)
            print(self.word_guessed)
            print(self.list_of_guesses)

new_game = Hangman(word_list)

new_game.ask_for_input()