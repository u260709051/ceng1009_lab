#import turtle
#ty=turtle.Turtle()
#wn=turtle.Screen()

#side=int(input("how many sides for the polygon?: "))
#lenght=int(input("lenght of the side: "))
#ty.color(input("pen color: "),input("filling color: "))

#ty.begin_fill()
#for i in range(side):
#    ty.fd(lenght)
#    ty.left(360/side)
#ty.end_fill()

#wn.exitonclick()  
# 


#import turtle
#ty=turtle.Turtle()
#wn=turtle.Screen()
#ty.pensize(3)

#for i in range (5):
#    ty.fd(150)
#    ty.right(144)

#wn.exitonclick()    

import turtle
ty=turtle.Turtle()
wn=turtle.Screen()

legs=int(input("how many legs for the spider?: "))
for i in range(legs):
    ty.fd(150)
    ty.fd(-150)
    ty.right(360/legs)

wn.exitonclick()    

