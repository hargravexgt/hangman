import milestone_2

def check_in_word(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess: {guess} is in the word")
        for letter in word.split():
            if letter == guess:
                idx = word.split().index(guess)
                self.word_guessed[idx] = guess
    else:
        print(f"Sorry, {guess} not in the word. Try again!")

def ask_for_input():
    result = None
    while True:
        if bool(result) == True:
            break
        guess = milestone_2.ask_for_guess()
        result = milestone_2.check_valid_guess(guess)
    return guess
