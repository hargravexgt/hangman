import random
import milestone_2

word_list = milestone_2.word_list

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(list(self.word)))

    def check_guess(self, guess):
        if guess.lower().strip() in self.word:
            print(f"Good guess. {guess} is in the word.")
            for i in range(len(self.word)):
                if guess.lower().strip() == self.word[i]:
                    self.word_guessed[i] = guess.lower().strip()
            self.num_letters += -1       
        else:
            self.num_lives += -1
            print(f"Sorry, {guess} is not in the word.")
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        guess = ''
        while True:
            guess = input("Choose a letter:")
            if guess.isalpha()==False or len(guess)!= 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives=num_lives)
    while True:
        print(game.word_guessed)
        if game.num_lives == 0:
            print("You lost. You ran out of lives.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f"Congratulations, you won the game! It took you {len(game.list_of_guesses)} guesses.")
            break

play_game(word_list)