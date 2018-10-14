from random import randint
e = randint(-1,1)
x = randint(0, 10)
y = randint(1, 10)
r = x + y + e 
print ('{0} + {1} = {2}'.format(x, y, r))
a = input ('Y/N:').upper()
if e == 0:
    if a == 'Y':
        print('True.')
    elif a == 'N':
        print('False.')
else:
    if a == 'Y':
        print('False.')
    elif a == 'N':
        print('True.')