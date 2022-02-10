import turtle

Colors=["orange","red","pink","yellow","blue","green"]

screen=turtle.Screen()
trtl=turtle.Turtle()
trtl.speed(0)
screen.bgcolor('black')

for i in range (360):
    trtl.pencolor(Color[x%6])
    trtl.width(x/5+1)
    trtl.forward(x)
    trtl.left(20)
