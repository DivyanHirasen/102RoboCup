import math
import turtle
import random

ran = random.Random()
ballSpeedMultiples = [0.5 , 0.75 , 1.25 , 1.72 , 2] 

gkSpeed = 4

def getDistance (x1 , y1 , x2 , y2) :                          #Returns straight line distince between two points on
    d = round ( math.sqrt ( (x2-x1)**2 + (y2-y1)**2 ) , 2 )    #the plane
    
    return d

def getTime( distance , speed ) :                              #Returns the time taken for the turtle to travel to a
    time = round ( (distance / speed) , 2 )                    #location on the plane ( units : cartesian units/turtle speed )
    
    return time

def getSavePoint(angle):                                        #Determines the Y-axis point of the balls trajectory
    distance =  math.tan( math.radians( abs(angle) ) ) * 500 
    distance = round ( distance , 2 ) 
  
    if abs(angle) == angle :                                    #Positive degree , moving up from perpendicular length
        savePoint = abs ( distance )                            #Negative degree , moving down from perpendicular length
    else :
        savePoint = (-1)*distance
    
    return savePoint

def drawField():
    
    pen = turtle.Turtle()
    pen.speed(0)
    #pen.hideturtle()
    pen.color("white")
    pen.shape("circle")
    pen.pensize(2)
    pen.penup()
    
    pen.goto(-200,100)
    pen.pendown()
    pen.circle(-80,180)
    pen.penup()
    
    pen.goto(400,100)
    pen.pendown()
    pen.circle(80,180)
    pen.penup()
        
    
    pen.goto(-400,0)
    
    
    
    #size of goalpost. If the size of goalpost is altered then the bounds for the angle at which the
    #ball is allowed to be projected at needs to be altered too. For goal post size = 226.5 , the bounds of
    #the angle of the balls trajectory is ( -24.37 , 24.37 ) inclusive
    sizeGoalPost = 226.5
    
    pen.pendown()
    pen.goto(-400,sizeGoalPost)
    #pen.write(str(pen.xcor()) +":"+ str(pen.ycor()))
    pen.goto(-400,(-1)*sizeGoalPost)
    point = pen.position()
    #pen.write(str(pen.xcor()) +":"+ str(pen.ycor()))
    #pen.hideturtle()
    pen.color("white")
    pen.shape("circle")
    pen.pensize(2)
    pen.setheading(0)
    pen.forward(200)
    pen.setheading(90)
    pen.forward(sizeGoalPost*2)
    pen.setheading(180)
    pen.forward(200)
    pen.setheading(90)
    pen.forward(60)
    pen.setheading(0)
    pen.forward(1000)
    pen.setheading(270)
    pen.forward(sizeGoalPost*2)
    pen.forward(60*2)
    pen.setheading(90)
    pen.forward(60)
    pen.setheading(180)
    pen.forward(200)
    pen.setheading(90)
    pen.forward(sizeGoalPost*2)
    pen.setheading(0)
    pen.forward(200)
    pen.setheading(270)
    pen.forward(sizeGoalPost*2)
    pen.forward(60)
    pen.setheading(180)
    pen.forward(1000)
    pen.setheading(90)
    pen.forward(60)
    
    pen.penup()
    pen.goto( 105 , 0 )
    pen.setheading(90)
    pen.forward(12)
    pen.setheading(180)
    pen.forward(10)
    
    pen.pensize(2)
    pen.pendown()
    
    pen.setheading(0)
    pen.forward(10)
    
    pen.setheading(315)
    pen.forward(10)
    
    pen.setheading(270)
    pen.forward(10)
    
    pen.setheading(225)
    pen.forward(10)
    
    pen.setheading(180)
    pen.forward(10)
    
    pen.setheading(135)
    pen.forward(10)
    
    pen.setheading(90)
    pen.forward(10)
    
    pen.setheading(45)
    pen.forward(10)
    
    pen.hideturtle()
    
    
def randomBallSpeed() :     # Returns random speed for the ball based on the speed of the goalkeeper
    global gkSpeed
    
    random.shuffle ( ballSpeedMultiples ) 
    randomSpeed = ran.randrange ( 0 , 4 )
    speed = gkSpeed * ballSpeedMultiples[randomSpeed]
     
    return speed    
                    
def move (angle , savePoint , s) :

    global ball
    global goalkeeper
    score = s
    score.clear()
    
    ball.setheading(180)                                #Ensures ball faces the goalpost
    goalkeeper.setheading(0)
    
    
    if angle < 0 :                                      #Alters the orientation of the ball according to the random angle
        ball.left ( abs ( angle ) ) 
    elif angle > 0 :
        ball.right ( abs ( angle ) )    
    
    if goalkeeper.ycor() > savePoint :                  #Goalkeeper moves down if the save location is below the 
        goalkeeper.right(90)                            #current location of the goalkeeper
        
        for reactionTime in range  (20) :                          #Reaction time of goalkeeper
            ball.forward ( ball.speed() )
            goalkeeper.goto ( goalkeeper.xcor() , goalkeeper.ycor() )
        
        while goalkeeper.ycor() > savePoint or ball.xcor() > goalkeeper.xcor(): #Iterate the ball and the       goalkeeper as  
            goalkeeper.forward( goalkeeper.speed() )                            #long as both did not reach the save 
            
            ball.forward( ball.speed() )                                        #location yet    
            
            if ball.xcor() <= goalkeeper.xcor() :        #Ball has reached the goalpost before goalkeeper
                ball.goto( goalkeeper.xcor() , savePoint )
                score.color("green")
                score.write("GOAL", font=('Arial', 15, 'normal'))
                while goalkeeper.ycor() > savePoint :       #Iterates the movement of just the goalkeeper
                    goalkeeper.forward( goalkeeper.speed() )
                    ball.goto ( goalkeeper.xcor() , savePoint )
                temp = goalkeeper.speed()               #Alters direction of goalkeeper to face the ball
                goalkeeper.speed(100)
                goalkeeper.left(90)  
                goalkeeper.speed(temp)                
            elif goalkeeper.ycor() <= savePoint :       #Goalkeeper has reached save point before ball
                temp = goalkeeper.speed()               #Alters direction of goalkeeper to face the ball
                goalkeeper.speed(100)
                goalkeeper.left(90) 
                goalkeeper.goto ( goalkeeper.xcor() , savePoint ) 
                goalkeeper.speed(temp)
                while ball.xcor() > goalkeeper.xcor() : #Iterates the movement of just the ball
                    ball.forward( ball.speed () )
                    goalkeeper.goto ( goalkeeper.xcor() , goalkeeper.ycor() )
                ball.goto( goalkeeper.xcor() , savePoint )
                score.color("red")
                score.write("SAVE", font=('Arial', 15, 'normal'))
                                
    elif goalkeeper.ycor() < savePoint :                #Goalkeeper moves up if save location is above the current
        goalkeeper.left(90) 
        #location of the goalkeeper
        for reactionTime in range (20) :                           #Reaction time of goalkeeper
            ball.forward( ball.speed() )
            goalkeeper.goto( goalkeeper.xcor() , goalkeeper.ycor() )
        
        while goalkeeper.ycor() < savePoint or ball.xcor() > goalkeeper.xcor() : #Iterate the ball and the goalkeeper 
            goalkeeper.forward( goalkeeper.speed() )                             #as long as both did not reach the save
            ball.forward ( ball.speed() )                                        #location yet
            
            if ball.xcor() <= goalkeeper.xcor() :                 #Ball has reached the goalpost before the goalkeeper
                ball.goto( goalkeeper.xcor() , savePoint )
                score.color("green")
                score.write("GOAL", font=('Arial', 15, 'normal'))
                while goalkeeper.ycor() < savePoint :             #Iterates the moveent of just the goalkeeper
                    goalkeeper.forward( goalkeeper.speed() )
                    ball.goto ( goalkeeper.xcor() , savePoint ) 
                temp = goalkeeper.speed()                           #Alters direction of goalkeeper to face the ball
                goalkeeper.speed(100)                 
                goalkeeper.right(90)   
                goalkeeper.speed(temp)                
            elif goalkeeper.ycor() >= savePoint :               #Goalkeeper has reached save point before ball
                temp = goalkeeper.speed()                       #Aters direction of goalkeeper to face the ball
                goalkeeper.speed(100)                 
                goalkeeper.right(90)  
                goalkeeper.goto ( goalkeeper.xcor() , savePoint )                 
                goalkeeper.speed(temp) 
                while ball.xcor() > goalkeeper.xcor() :         #Iterates movement of just the ball
                    ball.forward( ball.speed () )  
                    goalkeeper.goto ( goalkeeper.xcor() , goalkeeper.ycor() )                    
                ball.goto( goalkeeper.xcor() , savePoint ) 
                score.color("red")
                score.write("SAVE", font=('Arial', 15, 'normal'))
    
def shoot(gk , b , s):
    print("Shoot")
    
    global goalkeeper
    global ball
    global gkSpeed
    
    goalkeeper = gk
    ball = b
    
    #Sends ball back to original location ( 300 , 0 ) / Makes sure ball is in origonal position   
    ball.hideturtle()
    ball.speed(100)
    ball.goto(100,0)
    ball.showturtle()
    
    angle = round ( ran.uniform(-24.37,24.28) , 2 )         #Seecting random angle for trajectory of ball 
    savePoint = getSavePoint(angle)                         #The balls trajectory will meet the goalpost at
                                                            # (x,y) = ( -200 , savePoint ) 
    
    #Generate Random Speed for Ball         
    ball.speed(randomBallSpeed())                           #If equal to 0 then will get an error due to the distancespeed() )                                        #location yet    
            
    goalkeeper.speed(gkSpeed)                                     #calculation ... dividing by zero
    
    goalkeeperDistance = getDistance ( goalkeeper.xcor() , goalkeeper.ycor() , goalkeeper.xcor() , savePoint) 
    ballDistance = getDistance( 100 , 0 , goalkeeper.xcor() , savePoint )
       
    goalkeeperTime = getTime ( goalkeeperDistance , goalkeeper.speed())
    ballTime = getTime ( ballDistance , ball.speed())
    
    print("Angle : {0} \nSavepoint : -200 : {1}\n".format ( angle , savePoint ) )
    print("Ball speed : {0}\nGoalkeeper speed : {1}\n".format ( ball.speed() , goalkeeper.speed() ) )
    print("Goalkeeper distance : {0} \nBall distance : {1}\n".format( goalkeeperDistance , ballDistance ) )
    print("Goalkeeper time : {0} \nBall Time : {1}\n".format ( goalkeeperTime , ballTime ) ) 
    
    if ballTime < goalkeeperTime :                          #Outcome of the shot is already determined from the distances 
        print("Goal")                                       #of the bal and the goalkeeper from the save point and their 
    elif ballTime > goalkeeperTime:                         #speeds
        print("Save")
    else:
        print("Save")
        
    
    print("=====================================")
    
    move( angle , savePoint , s)                                #movement of the ball and the goalkeeper begin
                
       
def reset(gk , b, s):
    print("=====================================\nReset\n=====================================\n")
    
    global goalkeeper
    global ball
    
    score = s
    score.clear()
   
    goalkeeper = gk
    ball = b
    
    ball.hideturtle()
   
    goalkeeper.goto( goalkeeper.xcor() , round ( ran.uniform(226.5,-226.6) , 2 ) )
    #goalkeeper.write( str (goalkeeper.xcor()) +":"+str( goalkeeper.ycor() ) )
    
    ball.speed(100)
    ball.goto( 100 , 0 ) 
    
    ball.setheading(180)
    goalkeeper.setheading(0)
    
    ball.showturtle()
    
def exit():
    window.bye()
    print("=====================================\nExit\n=====================================\n")
