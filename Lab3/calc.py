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

    





# a = int(input("a = "))
# b = int(input("b = "))

# s = add(a, b)

# print (s)