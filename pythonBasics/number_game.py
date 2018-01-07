import random
# random.randint

random_number = random.randint(1, 10)
print(random_number)


def rules():
    print("""
Guess a number between 1 and 10!
If you give up type 'quit'
""")


def question():
    rules()
    while True:
        answer = input("> ")
        if answer == "quit":
            break
        elif int(answer) == random_number:
            print("CONGRATS YOU WON!!!")
            break
        
        print('BUZZZZ WRONG')
        continue

question()
    