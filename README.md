# Hangman Project

# Table of Contents
1. [Introduction](#introduction)
2. [Description of Project](#description-of-project)
3. [Installation instructions](#installation_instructions)
4. [Usage instructions](#usage-instructions)
5. [File Structure of Project](#file-structure-of-project)
6. [License Information](#license-information)



## Introduction

Welcome to my hangman project!

## Description of Project
Hangman AiCore Project

Each milestone is a stage of the project, slowly developing the hangman infrastructure. The final product can be found in `milestone_5.py`. 

The Hangman class initialises an instance of the game, requesting one argument: `word_list`. The `num_lives` argument is set at 5 by default. It has six attributes:
- word: The word to be guessed, picked randomly from the word_list. 
- word_guessed: list - A list of the letters of the word.
- num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
- num_lives: int - The number of lives the player has at the start of the game.
- word_list: list - A list of words
- list_of_guesses: list - A list of the guesses that have already been tried.

The Hangman class has two methods:
- check_guess(self, guess): this takes the guess as an argument and checks whether it is in the word. If it is then it informs you tht you made a good guess. If it isn't then it informs you that you missed, lost a life and informs you of your lives yet.
- ask_for_input(self): this doesn't take an argument but asks for input, namely, it asks for a guess. It then validates this guess, checking it is in a single, alphabetical character. If it is valid it calls the `check_guess(self, guess)` method with the guess as the argument before breaking the function. If it isn't valid it informs you and requests another guess that is a single, alphabetical character. Lastly, if the guess is valid but you have already made that guess, it informs you and once again asks for another guess.

The last function is the `play_game(word_list)` function that runs a complete game of hangman: it takes the `word_list` as an argument. It then initialises a Hangman instance with this `word_list` argument. Once again, `num_lives` attribute is set as 5. A `while True` loop is then used to run the game. It has three seperate conditions that run the game in different directions:
- if the player has 0 lives left: prints "You lost. You ran out of lives."
- if there are no letters left to guess: prints "Congratulations, you won the game! It took you {len(game.list_of_guesses)} guesses."
- if neither of these conditions hold, the game continues: it calls the `ask_input()` method of the game to request another guess.

Finally, `play_game(word_list)` is called with the `word_list` imported from the `milestone_2` module/file.


## Installation Instructions

The only required module is `random`. The file `milestone_5.py` imports this. It will need to be pre-installed on your local machine.

## Usage Instructions

To run the hangman game. Run `milestone_5.py`.

## File Structure of Project

    ├── milestone_5.py           #      
    ├── milestone_4.py           # 
    ├── milestone_3.py           #  
    ├── milestone_2.py           #      
    ├── LICENSE                  #
    └── README.md                #


## License Information
GNU GENERAL PUBLIC LICENSE

