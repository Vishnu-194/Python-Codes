
import turtle

col = ["red","yellow","green","cyan","pink","white"]

trtl = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
trtl.speed(25)

for i in range (150):
    
    trtl.color(col[i%6])
    trtl.forward(i*1.5)
    trtl.left(59)
    trtl.width(3)
