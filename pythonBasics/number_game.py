import random
# random.randint

random_number = random.randint(1, 10)
guesses = []
print(random_number)


def rules():
    print("""
Guess a number between 1 and 10!
If you give up type 'quit'

""")


        # cached_anwser = "empty"
def question():
    rules()

    while len(guesses) < 5:
        try:
            answer = int(input("> "))
        except ValueError:
            print("{} isn't a number!".format(answer))
        if answer == "quit":
            break
        else:
            if answer < random_number:
                print("Your last guess was {}. You were too low.".format(answer))
                continue
            elif answer > random_number:
                print("Your last guess was {}. You were too High!".format(answer))
            elif int(answer) == random_number:
                print("CONGRATS YOU WON!!!")
                print("The secret number was {}".format(random_number))
                break
            guesses.append(answer)
            continue
    else:
        print("You ran out of guesses")
    play_again = input("Do you want to play again? Y/n")
    if play_again.lower() != "n":
        question()
    else:
        print("Thanks for tying")

question()
    