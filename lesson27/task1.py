import turtle
import turtle as t
from time import sleep

screen = turtle.Screen()
screen.bgcolor('white')


heart = turtle.Turtle()
heart.color('red')
heart.fillcolor('red')
heart.speed(2)


def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(224)
    heart.circle(-96, 200)
    heart.left(120)
    heart.circle(-96, 190)
    heart.forward(192)
    heart.end_fill()


draw_heart()
t.mainloop()