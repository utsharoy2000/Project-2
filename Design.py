#ninja 2 ...........
import turtle 
turtle.bgcolor("black")

squary = turtle.Turtle()
squary. speed(20)
squary.pencolor("green")
for i in range( 400):
    squary.forward(i)
    squary.left(91)


import turtle
ninja = turtle.Turtle()
ninja.speed(20)
ninja.pencolor("red")
for i in range( 180):
        ninja.forward (100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)

        ninja.penup()
        ninja.setposition(0,0)
        ninja.pendown()


        ninja.right(2)

turtle.done()