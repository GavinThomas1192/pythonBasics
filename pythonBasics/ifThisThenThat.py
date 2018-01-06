age = 25 * 365

if age < 10000:
    print('Wow, you\'re young!', 'Age = {}'.format(age))
else:
    print('Wow, you\'re old!')


# Make admitted = true if age is 13

admitted = None

if age >= 13:
    admitted = True
else:
     print('Age isn\'t 13!')

days_open = ['Monday', 'Tuesday', 'Wednesday']
days_open_string = (', '.join(days_open))
today = 'Saturday'
if today in days_open:
    print('Come on In!')
else:
    print('Sorry we are closed {}'.format(today), 'But we are open {}'.format(days_open_string))