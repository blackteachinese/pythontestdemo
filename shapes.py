#!/usr/bin/python
import turtle
sides = int(raw_input("Enter ther number of sides for \
	you shape:"))
angle = 360.0 / sides
length = 400.0 / sides
turtle.fillcolor("blue")
turtle.begin_fill()
for side in range(sides):
	print(side)
	turtle.forward(length)
	turtle.right(angle)
turtle.end_fill()
turtle.done();