from turtle import *
#we want to paint a house

#step 1; draw a square

width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("hellow")
right(150)
forward(200)
left(120)
forward(200)

exitonclick()