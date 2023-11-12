import milestone_2

def check_in_word(guess, word):
    """ This fuction takes a guess and a word. If the guess is in the word it tells us and replkaces all the spaces where
    that letter is present in the word with the guessed letter. If it isn't in the word then it tells us. In either case it 
    returns our current guessed_word."""
    guess = guess.lower()
    guessed_word = ['_']*word
    if guess in word:
        print(f"Good guess: {guess} is in the word")
        for letter in word.split():
            if letter == guess:
                idx = word.split().index(guess)
                guessed_word[idx] = guess
    else:
        print(f"Sorry, {guess} not in the word. Try again!")
    return guessed_word


def ask_for_input():
    """ This function asks for a guess and checks whether its valid. If it is valid then it returns the guess,
    if it isn't then it notifies you that it isn't and makes another request for a guess."""
    result = None
    while True:
        if bool(result) == True:
            break
        guess = milestone_2.ask_for_guess()
        result = milestone_2.check_valid_guess(guess)
    return guess
