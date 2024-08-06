import os
import turtle
import time 
import random
import tkinter

delay = 0.1
score = 0
high_score = 0
bg_colors = ["green", "cyan", "red", "white", "black", "purple"]


window = turtle.Screen()
window.title("Snake")
window.bgcolor("cyan")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))

#Game functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"
    
def goLeft():
    if head.direction != "right":
        head.direction = "left"
    
def goRight():
    if head.direction != "left":
        head.direction = "right"
    
#Keybinds

window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goDown, "s")
window.onkeypress(goLeft, "a")
window.onkeypress(goRight, "d")

#Main loop  
while True:
    window.update()
    
    #Check borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:    
        time.sleep(1)
        head.goto(0,0)
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        head.direction = "stop"
        delay = 0.1
        
        # Hide segment
        for segment in segments:
            segment.goto(1000,1000)
            
        #Clear segment list
        segments.clear()
            
    #Collision with food
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x, y)
        
        #Snake grows
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("grey")
        newSegment.penup()
        segments.append(newSegment)
        
        delay -= 0.001
        #Increase score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    #Segments move
    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)
        
    #Move first segment to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #Check head and body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide segment
            for segment in segments:
                segment.goto(1000,1000)
            
            segments.clear()
            score = 0
            
            delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    time.sleep(delay)

window.mainloop()