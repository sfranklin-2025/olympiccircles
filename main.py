import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')
t=turtle
t.speed(8)

#circle1
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(0)


t.circle(50)
t.setheading(90)





#this changes turtle location
t.penup()
t.goto(0,0)
t.pendown()

#circle2

t.goto(80,0)
t.setheading(0)
t.pencolor('blue')

t.circle(50)


#this changes turtle location
t.penup()
t.goto(0,0)
t.pendown()


#circle3

t.goto(-80,0)
t.setheading(0)
t.pencolor('red')

t.circle(50)
t.setheading(90)

#circle4

t.goto(-45,-45)
t.setheading(0)
t.pencolor('yellow')

t.circle(50)
t.setheading(90)

#circle5


t.goto(45,-45)
t.setheading(0)
t.pencolor('green')

t.circle(50)
t.setheading(90)

#text
t.penup()
t.goto(0,200)
t.pencolor('purple')
t.pendown()
t.write("Winter Olympics",font=("arial",25,"bold italic"),align="center")




turtle.done()
