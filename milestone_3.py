import milestone_2

word = milestone_2.random_word()

result = None

while True:
    if bool(result) == True:
        print(result)
        break
    guess = milestone_2.ask_for_guess()
    result = milestone_2.check_guess(guess)

print(guess)
