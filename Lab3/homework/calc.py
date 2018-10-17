from random import randint, choice
def add(x,y):
    r = x + y
    return(r)
def eval(x, y, op):
    if op == "+":
        r  = x + y
    elif op == '-':
        r = x - y
    elif op == '*':
        r = x * y 
    elif op == '/':
        r = x / y
    return r

r = add(1,2)
print(r)