letters = 'abcdefg'

for letter in letters:
    print(letter.upper())
# **********
numbers = [1,2,3,4]

for num in numbers:
    if num % 2 == 0:
        print('This number is even {}'.format(num)) 

# **********

start = 10
while start:
    print(start)
    start -= 1

# **********

names= ['Gavin', 'Shaun', 'Alli', 'Amy']

for name in names:
    if name == 'Alli':
        break
    print(name)
    
print('NEW TEST')
# ********** This skips over the name alli and continues on 
for name in names:
    if name == 'Alli':
         continue
    print(name)