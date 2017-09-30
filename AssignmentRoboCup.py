
import turtle 
import math
import random
import rcMod

window = turtle.Screen()
goalkeeper = turtle.Turtle()
ball = turtle.Turtle()

information = turtle.Turtle()           #Display controls
information.hideturtle()

score = turtle.Turtle()                 #Display shot outcome

def main () :
    turtle.setup(1300,700)
    window.bgcolor("darkgreen")
    window.title("RoboCup COMP102")
    ran = random.Random()
    
    #Creating score info
    score.penup()
    score.hideturtle()
    score.goto ( -550 , 100 ) 
    
    #Creating Goalkeeper
    goalkeeper.hideturtle()
    goalkeeper.penup()
    goalkeeper.goto(--400,0)
    goalkeeper.color("red")
    goalkeeper.shape("triangle")
    goalkeeper.shapesize(0.75)
    
    goalkeeper.goto(-400 , round ( ran.uniform(226.5,-226.6) , 2 ) )
    #goalkeeper.write(str(goalkeeper.xcor()) +":"+ str(goalkeeper.ycor()))
     
    goalkeeper.showturtle()
    
    #Creating Ball 
    ball.hideturtle()
    ball.color("yellow")
    ball.shape("circle")
    ball.shapesize(0.7)
    ball.penup()
    
    ball.goto(100,0)
    #ball.write(str(ball.xcor()) +":"+ str(ball.ycor()))
    
    ball.showturtle() 
    
    information.penup()
    information.goto(-550 , 190 ) 
    information.write("Shoot : {0}\nReset : {1}\nQuit   : {2}".format( "S" , "R" , "Q" ), font=('Arial', 10, 'normal'))
    information.hideturtle()
    
#Event Handlers    
def exit():
    window.bye()
    print("exit")
    
def shoot () :
    rcMod.shoot(goalkeeper ,  ball , score)
    
def reset () :
    rcMod.reset(goalkeeper , ball , score)
   


if __name__ == '__main__' :
    main()

rcMod.drawField()

#Keys
window.onkey(exit, "q")
window.onkey(reset , "r")
window.onkey(shoot, "s" )

#Listening for events
window.listen()
window.mainloop()
