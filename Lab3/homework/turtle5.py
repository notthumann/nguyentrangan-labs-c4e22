from turtle import *
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for _ in range(5):
        forward(length)
        right(144)

draw_star(10,100,100)
mainloop()
