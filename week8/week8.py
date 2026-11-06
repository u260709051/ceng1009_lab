# def gradeMark(mark):
#
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# marks=[95,90,89.9,80,79.9,70,65,60,59.5,0]
# for i in marks:
#     print("grade is", gradeMark(marks))
#
# mark=(float(input("what is your mark? ")))
# print("grade is", gradeMark(mark))





# import turtle
# def chooseColor(height):
#     if height>=200:
#         return "red"
#     elif height>=100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t,height,gap):
#
#     t.penup()
#     t.left(90)
#     t.forward(height +gap)
#     t.write(" "+str(height))
#     t.backward(height +gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height=(max(data))
#     num_bars=len(data)
#     border=10
#     gap=(max_height+border)/25
#
#     wn=turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right=(40 * num_bars + border)
#     top = (max_height + 4 * border)
#     wn.setworldcoordinates(-border,-border,right,top)
#     ty=turtle.Turtle()
#     ty.color("blue")
#     ty.pensize(3)
#     ty.speed(0)
#     for height in data:
#             drawBar(ty,height,gap)
#
#     wn.exitonclick()
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)





# import turtle
# def chooseColor(height):
#     if height>=200:
#         return "red"
#     elif height>=100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t,height,gap):
#     if height>=0:
#         labelY=height + gap
#     else:
#         labelY=gap
#
#
#     t.penup()
#     t.left(90)
#     t.forward(labelY)
#     t.write(" "+str(height))
#     t.backward(labelY)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height=(max(data))
#     min_height=(min(data))
#     num_bars=len(data)
#     border=10
#     gap=(max_height+border)/25
#
#     wn=turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right=(40 * num_bars + border)
#     top = (max_height + 4 * border)
#     bottom=min(min_height,0)-border
#
#     wn.setworldcoordinates(-border,bottom,right,top)
#     ty=turtle.Turtle()
#     ty.color("blue")
#     ty.pensize(3)
#     ty.speed(0)
#     for height in data:
#         drawBar(ty,height,gap)
#
#     wn.exitonclick()
#
# data = [48, -117, 140, 240, -50, 260, 120]
# barChart(data)


def findHypot(edge1, edge2):
    r=(edge1**2+edge2**2)**0.5
    return r
print(findHypot(4,3))

import math
def findHypotMath(edge1, edge2):
    r= math.sqrt(edge1**2+edge2**2)
    return r
print(findHypotMath(4,3))