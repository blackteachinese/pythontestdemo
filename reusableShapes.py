#!/usr/bin/python
import turtle
import random
def drawShape(sides, length):
	angle = 360.0 / sides
	for side in range(sides):
		turtle.forward(length)
		turtle.right(angle)
def moveTurtle(x, y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
def drawSquare(length):
	drawShape(4, length)
def drawTriangle(length):
	drawShape(3, length)
def drawCircle(length):
	drawShape(360, length)


# drawShape(4,10)
# moveTurtle(60, 30)
# drawShape(3, 20)
# moveTurtle(-10,-50)
# drawShape(9,15)

# moveTurtle(80, 40)
# drawTriangle(4)
# moveTurtle(100, 50)
# drawCircle(27)
# turtle.done();
def drawRandom():
	x = random.randrange(-200,200)
	y = random.randrange(-200,200)
	length = random.randrange(75)
	shape = random.randrange(1,4)
	print (length)
	# print " x = " + string(x) + " y= " + y + " length " + length + " shape = " + shape
	moveTurtle(x,y)
	if shape == 1:
		drawSquare(length)
	elif shape == 2:
		drawTriangle(length)
	elif shape == 3:
		length = length % 4
		drawCircle(length)


for shape in range(100):
	turtle.fillcolor("red")
	turtle.begin_fill()
	drawRandom()
	turtle.end_fill()
turtle.done()