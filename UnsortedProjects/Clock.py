# Python Class 2231
# Lesson 3 Problem 7
# Author: Skyparker (464417)
import turtle
import time
wn = turtle.Screen()      
t = turtle.Turtle()    #setup
t.speed(0)    #To draw fast
wn.tracer(0)

t.left(90)
def drawClock(hour, minutes, seconds):
 for x in range(12):
    #draw ticks
    t.penup()
    t.forward(200)
    t.stamp()
    t.forward(-200)
    t.right(30)
#minutes hand \/
 t.pensize(2)
 t.pencolor("black")
 t.right(minutes * 6)
 t.pendown()
 t.forward(120)
 t.forward(-120)
 t.left(minutes * 6)
#hour hand
 t.pensize(4)
 t.pencolor("black")
 t.right(hour*30+minutes*0.5)
 t.forward(100)
 t.forward(-100)
 t.left(hour*30+minutes*0.5)
#seconds hand
 t.pensize(1)
 t.pencolor("black")
 t.right(seconds * 6)
 t.pendown()
 t.forward(150)
 t.forward(-150)
 t.left(seconds * 6)
 t.pencolor("black")
 
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    drawClock(h,m,s)
    wn.update()
    time.sleep(1)
    t.clear()
    
