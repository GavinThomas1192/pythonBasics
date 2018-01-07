import random
words = ['apple', 'bannana', 'orange', 'coconut', 'lemon', 'melon']

while True:
    start = input("Press enter/return to start, or enter to Q to quit ")
    if start.lower() == "q":
        break

        # This is pretty awesome, chooses a random item from words array 
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses =[]

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print("")
        print("Strikes: {}/7".format(len(bad_guesses)))
        print("")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Sorry, guesses may only be one letter")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You did it! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didnt guess it, my secret word was {}".format(secret_word))