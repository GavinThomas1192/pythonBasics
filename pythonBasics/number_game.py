import random
# random.randint

random_number = random.randint(1, 10)
print(random_number)


def rules():
    print("""
Guess a number between 1 and 10!
If you give up type 'quit'

""")


        # cached_anwser = "empty"
def question():
    rules()
    while True:
        try:
            answer = int(input("> "))
        except ValueError:
            print("{} isn't a number!".format(answer))
        if answer == "quit":
            break
        elif answer < random_number:
            print("Your last guess was {}. You were too low.".format(answer))
            continue
        elif answer > random_number:
            print("Your last guess was {}. You were too High!".format(answer))
        elif int(answer) == random_number:
            print("CONGRATS YOU WON!!!")
            print("The secret number was {}".format(random_number))
            break
        
        print('BUZZZZ WRONG')
        continue

question()
    