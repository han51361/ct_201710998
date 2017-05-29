import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
width =wn.window_width()
print width

x1 = 0.0 -( width - 40)/3
x2 = 0.0
x3 =0.0 +( width - 40)/3

def drawSquare(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    for i in range(1,5) :
         t1.fd(size)
         t1.right(90)

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    for i in range(1,4) :
            t1.right(120)
            t1.fd(size)
 
    
def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    for i in range(1,6) :
            t1.right(144)
            t1.fd(size)
   

drawSquare(x1,100,100)
drawTriangleAt(x2,100,100)
drawStarAt(x3,100,100)

win.exitonclick()

