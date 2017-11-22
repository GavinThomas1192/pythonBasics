def add(num1, num2):
    #"try" to convert the numbers into floats...
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        #if we can't, we return None
        return None
    else:
        #otherwise....
        return num1+num2


works = add(1, 2,)
not_works = add('one', 'two')

print(works, not_works)
