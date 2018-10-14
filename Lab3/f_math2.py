from random import randint
op_list = ['+','-','*','/']
n = randint(0,3)
e = randint(-1,1)
x = randint(0, 10)
y = randint(1, 10)
if n == 0:
    r = x + y + e
elif n == 1:
    r = x - y + e
elif n == 2:
    r = x * y + e
else:
    r = x / y + e

print ( x, op_list[n], y , '=', r)

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