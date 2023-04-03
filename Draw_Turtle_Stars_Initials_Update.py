# Imports turtle module
import turtle as t

# Show the turtle on the screen
t.showturtle()

# Set the background color to red
t.bgcolor("red")

# Draw the letter S
t.penup()
t.setpos(10, 5)
t.pendown()
t.pensize(15)
t.color("whitesmoke")
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Move to the next location to draw the letter G
t.penup()
t.goto(40, -70)
t.pendown()

# Set the background color to firebrick
t.bgcolor("firebrick")

# Draw the letter G
t.pensize(12)
t.color("slategray")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.right(90)
t.forward(15)
t.left(90 * 2)
t.forward(30)

# Move to the next location to draw the first star
t.penup()
t.goto(100, -50)
t.pendown()
t.left(100)

# Set the background color to maroon
t.bgcolor("maroon")

# Draw the first star
t.pensize(6)
t.color("black")
for i in range(5):
    t.forward(300)
    t.right(144)

# Move to the next location to draw the second star
t.penup()
t.goto(80, -120)
t.pendown()
t.left(100)

# Set the background color to darkred
t.bgcolor("darkred")

# Draw the second star
t.pensize(6)
t.color("black")
for i in range(5):
    t.forward(300)
    t.right(144)

# Move to the next location to draw the circle
t.penup()
t.goto(-350, -100)
t.pendown()

# Set the background color to #bf0404
t.bgcolor("#bf0404")

# Draw the circle
t.pensize(10)
t.speed(5)
t.color('black')
t.circle(-350)
t.end_fill()

# End the program
t.done()