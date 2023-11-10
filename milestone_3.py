import milestone_2

word = milestone_2.random_word()

def check_in_word(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess: {guess} is in the word")
        return True
    else:
        print(f"Sorry, {guess} not in the word. Try again!")
        return False

def ask_for_input():
    result = None
    while True:
        if bool(result) == True:
            print(result)
            break
        guess = milestone_2.ask_for_guess()
        result = milestone_2.check_valid_guess(guess)
    return guess