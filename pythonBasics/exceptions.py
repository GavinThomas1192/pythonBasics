# ********************* The except will fire if ValueError is true, otherwise it will run the else

try:
    count = int(input('Give me a number: '))
except ValueError:
    print('That is not a number:')
else:
    print('Hi ' * count)