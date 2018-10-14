from random import randint,choice
from calc import eval
def generate_quiz():
    x = randint(0,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])
    error = randint (-1,1)
    r = eval (x , y, op) + error
    return [x,y,op,r]

quiz = generate_quiz()
x, y , op ,r = quiz
print(quiz)

