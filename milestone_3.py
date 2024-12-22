import milestone_2

def check_guess(guess, word):
    """
    This function takes a guess and a word as input, and then checks if the guess is in the word. If it is
    it tells us with a print message that it is; and if it isn't it tells us so with a printed message that 
    it isn't.
    """
    if guess.lower() in word.lower():
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """
    This function asks for an input. It checks if the input is valid. For it to be valid it needs to be a
    single alphabetical letter. If it isn't valid, then it tells us so and asks for a new input. This continues
    iteratively until a valid guess is given. Once a valid guess is given it calls the check_guess() function with
    the valid guess as the first argument and the randomly chosen word as the second argument.
    """
    guess = ''
    while True:
        guess = input("Choose a letter:")
        if guess.isalpha() and len(guess)== 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, word)

word = milestone_2.word # Importing randomly chosen word from word list in milestone_2.py
ask_for_input() # Calling ask_input() which includes check_guess()