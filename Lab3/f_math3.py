from random import randint, choice
from calc import eval

op = choice(['+','-','*','/'])
e = randint(-1,1)
x = randint(0, 10)
y = randint(1, 10)
t = eval (x , y , op)
r = t + e
print ( x , op , y, '=',r)

a = input ('Y/N:').upper
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