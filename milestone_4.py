import random

import milestone_2
import milestone_3

fruits  = ["Apple", "Kiwi", "Banana", "Watermelon", "Mango"]

class Hangman:
    def __init__(self, word_list, nl):
        self.word_list = word_list
        self.num_lives = nl
        self.word = milestone_2.random_word(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_in_word(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess: {guess} is in the word")
            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives += -1
            print(f"Sorry, {guess} not in the word. Try again!")
            print(f"You have {self.num_lives} left")


    def ask_for_input(self):
        guess = milestone_3.ask_for_input()
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_in_word(guess)
            self.list_of_guesses.append(guess)
            print(f"The word: {self.word_guessed}")
            print(f"Letters used: {self.list_of_guesses}")

def play_game(word_list):
    num_lives = 5
    new_game = Hangman(word_list, num_lives)
    while True:
        if new_game.num_lives == 0:
            print("You lost!")
            break
        elif new_game.num_letters > 0:
            new_game.ask_for_input()
        else:
            print(f"Congratulations. You won the game. Your word was {new_game.word}")
            break

play_game(fruits)

