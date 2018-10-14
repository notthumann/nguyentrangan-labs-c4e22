from calc import *
x = int(input('Enter a number: '))
y = int(input ('Enter a number: '))
s = x + y
print ("{0} + {1} = {2}".format(x,y,s))
o = input('Enter a operator: ')
r = eval(x,y,o)
print (x, o , y , '=', r)