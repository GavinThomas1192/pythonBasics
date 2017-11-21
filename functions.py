# **********
def hows_the_parrot():

    print('Hi im a parrot')


hows_the_parrot()


# **********


def lumber_jack(name):
    if name.lower() == 'gavin':
        print('HI {}'.format(name))
    else:

        print('Hi {}, but your not who Im looking for, go away {}'.format(name, name))


lumber_jack('Gavin')
lumber_jack('Jack')

# **********


def average(num1, num2):
    return(num1 + num2) / 2


avg = average(2, 2)
print(avg)
