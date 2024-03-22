from turtle import *
import turtle

import math

t = turtle.Turtle()
w = turtle.Screen()

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

t.penup()
t.goto(xc, yc)
t.pendown()
t.circle(r)

t.penup()
t.goto(x, y)
t.pendown()
t.dot()

d = math.sqrt((x-xc)**2 + (y-yc)**2)

if d < r:
    print('Точка находится внутри окружности')
elif d == r:
    print('Точка лежит на окружности')
else:
    print('Точка находится за пределами окружности')

w.mainloop()
