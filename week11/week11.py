from lib2to3.fixes.fix_zip import FixZip


def fizz_buzz(n):
    for i in range(1,n+1):
        if i%15==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
#fizz_buzz(30)

def digit_sum(n):
    total= 0
    while n>0:
        total=total+n%10
        n=n//10
        print(n)
    return total
#print(digit_sum(1234))

def alternate_case(s):
    result=""
    for i in range(len(s)):
        if i%2==0:
            result=result+s[i].upper()
        else:
            result=result+s[i].lower()
    return result
#print(alternate_case("hello world!"))

def drawPolygon(t,sides,lenght):
    for i in range(sides):
        t.forward(lenght)
        t.left(360/sides)

# import turtle
# ty=turtle.Turtle()
# wn=turtle.Screen()
# ty.pensize(3)
# wn.bgcolor("lightgreen")
# colors=["red","yellow","blue"]
# for i in range(3):
#     ty.penup()
#     ty.goto(-150+i*120,-30)
#     ty.pendown()
#     ty.color(colors[i])
#     drawPolygon(ty,i+3,70)
# wn.exitonclick()


def filledSquare(t,size,color):
    t.fillcolor(color)
    t.begin_fill()

    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# import turtle
# ty=turtle.Turtle()
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
#
# for i in range(5):
#     if i%2==0:
#         color = "red"
#     else:
#         color = "blue"
#     ty.penup()
#     ty.goto(-165 + i*70, -25)
#     ty.pendown()
#
#     filledSquare(ty,50,color)
#     ty.penup()
#     ty.forward(70)
#     ty.pendown()
#
#
# wn.exitonclick()


def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

# import turtle
# t=turtle.Turtle()
# t.pensize(2)
# t.speed(0)
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
#
# for i in range(12):
#     draw_square(t,80)
#     t.left(30)
#
# wn.exitonclick()


def draw_square(t, size,filled):
    if filled:
        t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    if filled:
        t.end_fill()

import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
t=turtle.Turtle()
t.speed(0)
size=40
for row in range(6):
    for col in range(6):
        t.penup()
        t.goto(-120+col*size,-120+row*size)
        t.pendown()
        draw_square(t,size,((row+col)%2==0))

wn.exitonclick()