# def add(num1, num2):
#     #"try" to convert the numbers into floats...
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#     except ValueError:
#         #if we can't, we return None
#         return None
#     else:
#         #otherwise....
#         return num1+num2


# works = add(1, 2,)
# not_works = add('one', 'two')

# print(works, not_works)

# import random
# def random_item(ite):
#     random_number = random.randint(0, (len(ite) - 1))
#     return ite[random_number]



# random_item(['hi', 'hi', 'hi'])

# this does not
# import sys
# def start_movie():
#     answer = input("Do you want to start the movie? ")
#     if answer != 'n' or answer != 'N':
#         print("Enjoy the show!")
#     else:
#          sys.exit()

# start_movie()

# this works
import sys
def start_movie():
    answer = input("Do you want to start the movie? ")
    if answer == 'n' or answer == 'N':
         sys.exit()
    else:
        print("Enjoy the show!")

start_movie()