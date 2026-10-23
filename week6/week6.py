import turtle
#--setup--
ty=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")
ty.speed(0)


#--functuions--

def drawPoly(t,side,somesize):
    angle=360/side
    for i in range(side):
        t.fd(somesize)
        t.left(angle)

def drawSpiral(t,angle):
    size=1
    for i in range(100):
        ty.fd(size)
        ty.right(angle)
        size+=3


def drawEquitriangle(t,somesize):
    drawPoly(t,3,somesize)


def drawStar(t,size):
    for i in range(5):
        t.fd(size)
        t.right(144)


def drawSprite(t,legs,size):
    angle=360/legs
    for i in range(legs):
        t.fd(size)
        t.fd(-size)
        t.left(angle)

#--exercises--
#Exercise 1
# ty.color("hotpink")
# ty.pensize(3)
# drawPoly(ty,8,50)

#Exercise 2
# ty.color("blue")
# ty.pensize(3)
# for i in range(24):
#     drawPoly(ty,4,100)
#     ty.left(360/24)

#Exercise3
# ty.penup()
# ty.goto(-170,0)
# ty.pendown()
# ty.color("blue")
# ty.pensize(2)
# drawSpiral(ty,90)
#
# ty.penup()
# ty.goto(170,0)
# ty.pendown()
# drawSpiral(ty,89)

#Exercise4
# drawEquitriangle(ty,100)

#Exercise5
# ty.pensize(3)
# ty.color("hotpink")
# ty.penup()
# ty.goto(-175,100)
# ty.pendown()
# for i in range(5):
#
#     drawStar(ty,100)
#     ty.penup()
#     ty.fd(350)
#     ty.right(144)
#     ty.pendown()

#Exercise6
# ty.pensize(2)
# drawSprite(ty,15,120)


#--finish--
wn.exitonclick()