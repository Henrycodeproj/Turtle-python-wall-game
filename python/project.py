import turtle
import random
import time
# designed and coded by Henry Li

#wall counters variables for functions, didnt work inside function, keep here.
p2counter = 0
p1counter = 0

def game():
  #screen settings
  screen = turtle.getscreen()
  screen.title("Henry's first project")
  screen.setup(width=600, height=600)
  screen.bgcolor("black")
  screen.tracer(0)

  #scores counter
  player1 = 0
  player2 = 0

  # first player
  The_turtle = turtle.Turtle()
  The_turtle.shape("turtle")
  The_turtle.color("blue")
  The_turtle.speed(0)
  The_turtle.penup()
  The_turtle.goto(265,220)

  #second player
  second_turtle = The_turtle.clone()
  second_turtle.shape("turtle")
  second_turtle.color("green")
  second_turtle.goto(-276,-260)

  #random food spawn
  randnum = random.randint(-250,250)
  randnum2 = random.randint(-200,200)
  ball = turtle.Turtle()
  ball.penup()
  ball.color("white")
  ball.shape("circle")
  ball.goto(randnum,randnum2)

  #scores table 
  scores = turtle.Turtle()
  scores.penup()
  scores.color("white")
  scores.goto(0,280)
  scores.hideturtle()
  scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1,player2), align = "center", font=  ("courier",10,"normal"))

  #Game timer
  timer = turtle.Turtle()
  timer.hideturtle()
  timer.setpos(-120,250)
  timer.color("white")

  #player1 walls
  blockp1 = turtle.Turtle()
  blockp1.shape("square")
  blockp1.shapesize(.01,2.5)
  blockp1.color("blue")
  blockp1.penup()
  blockp1.setpos(700,700)
  p1wall1 = blockp1.clone()
  p1wall2 = blockp1.clone()
  p1wall3 = blockp1.clone()
  p1wall4 = blockp1.clone()
  p1wall5 = blockp1.clone()

  #player2 walls
  blockp2 = turtle.Turtle()
  blockp2.shape("square")
  blockp2.shapesize(.01,2.5)
  blockp2.color("green")
  blockp2.penup()
  blockp2.setpos(700,700)

  p2wall1 = blockp2.clone()
  p2wall2 = blockp2.clone()
  p2wall3 = blockp2.clone()
  p2wall4 = blockp2.clone()
  p2wall5 = blockp2.clone()

  #white outside borders for the entire game
  border1 = turtle.Turtle()
  border1.color("white")
  border1.shape("square")
  border1.shapesize(.25,29.45,1)
  border1.penup()
  border1.setpos(0,-290)


  border2 = turtle.Turtle()
  border2.color("white")
  border2.shape("square")
  border2.shapesize(.25,29.64,1)
  border2.penup()
  border2.setpos(-2.5,245)


  border3 = turtle.Turtle()
  border3.color("white")
  border3.shape("square")
  border3.setheading(90)
  border3.shapesize(.25,27,1)
  border3.penup()
  border3.setpos(289,-25)

  border4 = turtle.Turtle()
  border4.color("white")
  border4.shape("square")
  border4.setheading(90)
  border4.shapesize(.25,27,1)
  border4.penup()
  border4.setpos(-297,-25)

  #directional functions for blue turtle/first turtle
  def first_turtle_up():
    The_turtle.speed(0)
    if The_turtle.setheading != (90):
      The_turtle.setheading(90)
      if The_turtle.heading():
        y = The_turtle.ycor()
        y += 10
        The_turtle.sety(y)

  def first_turtle_down():
    The_turtle.speed(0)
    if The_turtle.setheading != (270):
      The_turtle.setheading(270)
      if The_turtle.heading():
        y = The_turtle.ycor()
        y += -10
        The_turtle.sety(y)

  def first_turtle_right():
    The_turtle.speed(0)
    if The_turtle.setheading !=(0):
      The_turtle.setheading(0)
      if The_turtle.heading():
        x = The_turtle.xcor()
        x += 10
        The_turtle.setx(x)
      else:
        x = The_turtle.xcor()
        x += 10
        The_turtle.setx(x)

  def first_turtle_left():
    The_turtle.speed(0)
    if The_turtle.setheading !=(180):
      The_turtle.setheading(180)
      if The_turtle.heading():
        x = The_turtle.xcor()
        x += -10
        The_turtle.setx(x)

  #directional functions for green/second turtle
  def up():
    second_turtle.speed(0)
    if second_turtle.setheading != (90):
      second_turtle.setheading(90)
      if second_turtle.heading():
        y = second_turtle.ycor()
        y += 10
        second_turtle.sety(y)

  def down():
    second_turtle.speed(0)
    if second_turtle.setheading != (270):
      second_turtle.setheading(270)
      if second_turtle.heading():
        y = second_turtle.ycor()
        y += -10
        second_turtle.sety(y)

  def left():
    second_turtle.speed(0)
    if second_turtle.setheading !=(180):
      second_turtle.setheading(180)
      if second_turtle.heading():
        x = second_turtle.xcor()
        x += -10
        second_turtle.setx(x)

  def right():
    global player2
    second_turtle.speed(0)
    if second_turtle.setheading !=(0):
      second_turtle.setheading(0)
      if second_turtle.heading():
        x = second_turtle.xcor()
        x += 10
        second_turtle.setx(x)
      else:
        x = second_turtle.xcor()
        x += 10
        second_turtle.setx(x)


  # function for creating walls for blue/first turtle
  
  def space(): #pressing spacebar for blue turtle will create walls
    global p1counter #keeps track of how many walls are in place for green/first turtle
    if p1counter == 0:
      p1wall1.goto(The_turtle.xcor(),40+The_turtle.ycor())
      p1wall1.setheading(The_turtle.heading())
    if p1counter == 1:
      p1wall2.goto(The_turtle.xcor(),40+The_turtle.ycor())
      p1wall2.setheading(The_turtle.heading())
    if p1counter == 2:
      p1wall3.goto(The_turtle.xcor(),40+The_turtle.ycor())
      p1wall3.setheading(The_turtle.heading())
    if p1counter == 3:
      p1wall4.goto(The_turtle.xcor(),40+The_turtle.ycor())
      p1wall4.setheading(The_turtle.heading())
    if p1counter == 4:
      p1wall5.goto(The_turtle.xcor(),40+The_turtle.ycor())
      p1wall4.setheading(The_turtle.heading())
    p1counter += 1
    if p1counter == 5:
      p1counter = 0

  #function for creating walls for green/second turtle

  #keeps track of how many walls are in place for green/first turtle
  def zero(): #pressing number 0 for green turtle will create walls
    global p2counter
    if p2counter == 0:
      p2wall1.goto(second_turtle.xcor(),40+second_turtle.ycor())
      p2wall1.setheading(second_turtle.heading())
    if p2counter == 1:
      p2wall2.goto(second_turtle.xcor(),40+second_turtle.ycor())
      p2wall2.setheading(second_turtle.heading())
    if p2counter == 2:
      p2wall3.goto(second_turtle.xcor(),40+second_turtle.ycor())
      p2wall3.setheading(second_turtle.heading())
    if p2counter == 3:
      p2wall4.goto(second_turtle.xcor(),40+second_turtle.ycor())
      p2wall4.setheading(second_turtle.heading())
    if p2counter == 4:
      p2wall5.goto(second_turtle.xcor(),40+second_turtle.ycor())
      p2wall5.setheading(second_turtle.heading())
    p2counter += 1
    if p2counter == 5:
      p2counter = 0


  def restart():
    choice = turtle.textinput('Game Restart','Type yes if you would like to play again')
    if choice == 'yes':
      screen.clear()
      game()
    elif choice == None:
      exit()
    else:
      exit()

  #keyboardinputs for direction and wall making
  screen.onkeypress(first_turtle_up, 'w')
  screen.onkeypress(first_turtle_down, 's')     #blue turtle/first turtle
  screen.onkeypress(first_turtle_right, 'd')
  screen.onkeypress(first_turtle_left, 'a')
  screen.onkeypress(space, 'space')
  screen.listen()

  #screen.onkeypress()
  screen.onkeypress(up, "Up")
  screen.onkeypress(down, "Down")               #second turtle/green turtle
  screen.onkeypress(right, "Right") 
  screen.onkeypress(left, "Left")    
  screen.onkeypress(zero, "0") 
  screen.listen()

  #timer

  start_time = time.time()  #gets current time passed since starting
  time_limit = 180 #seconds

  #main Loop

  while True:
    total_time = time.time() - start_time
    remaining_time = time_limit - total_time
    timer.clear()
    timer.write("Total time left in seconds {}".format(int(remaining_time)), font = 20)
    screen.update()

  #food interactions and scoring

    if The_turtle.distance(ball) < 20: #first turtle
      x = random.randint(-265,265)
      y = random.randint(-240,240)
      ball.goto(x,y)
      player1 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))
    if second_turtle.distance(ball) < 20: #second
      x = random.randint(-265,265)
      y = random.randint(-240,240)
      scores.clear()
      player2 += 1 
      ball.goto(x,y)
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

  #player 1 wall interactions to player 2, resets score and spawns turtle and food in new location

    if second_turtle.distance(p1wall1) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      second_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player1 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if second_turtle.distance(p1wall2) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      second_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      scores.clear()
      player1 += 1
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align ="center",    font =("courier",10,"normal"))

    if second_turtle.distance(p1wall3) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      second_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player1 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if second_turtle.distance(p1wall4) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      second_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player1 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if second_turtle.distance(p1wall5) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      second_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player1 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

  #player 2 wall interactions to player 1
    if The_turtle.distance(p2wall1) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      The_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player2 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if The_turtle.distance(p2wall2) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      The_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player2 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if The_turtle.distance(p2wall3) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      The_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player2 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center",     font =("courier",10,"normal"))

    if The_turtle.distance(p2wall4) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      The_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player2 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center", font =("courier",10,"normal"))

    if The_turtle.distance(p2wall5) < 20:
      ball.goto(random.randint(-265,265),random.randint(-240,240))
      The_turtle.goto(random.randint(-265,265),random.randint(-240,240))
      player2 += 1
      scores.clear()
      scores.write("Player 1(Blue):{}  Player 2(Green):{}".format (player1, player2), align = "center", font =("courier",10,"normal"))

    #game timer
    if total_time > time_limit:
      if player1 > player2:
        finalpageP1 = turtle.Turtle()
        finalpageP1.hideturtle()
        finalpageP1.penup()
        finalpageP1.color("white")
        finalpageP1.write("Congratulations! Player 1 has won with {}".format(player1) + " point(s)",  align="center", font = 30)
        restart()

      elif player2 > player1:
        finalpageP1 = turtle.Turtle()
        finalpageP1.hideturtle()
        finalpageP1.penup()
        finalpageP1.color("white")
        finalpageP1.write("Congratulations! Player 2 has won with {}".format(player2) + " point(s)", align    ="center", font = 30)
        restart()

      else:
        finalpageP1 = turtle.Turtle()
        finalpageP1.hideturtle()
        finalpageP1.penup()
        finalpageP1.color("white")
        finalpageP1.write("It's a tie, no one wins!", align ="center", font = 30)
        restart()

    #borders for both turtles
    if The_turtle.xcor() < -280:
       The_turtle.backward(20)
    if The_turtle.xcor() > 270:
      The_turtle.backward(20)
    if The_turtle.ycor() < -260:
      The_turtle.backward(20)
    if The_turtle.ycor() > 220:
      The_turtle.backward(20)
    if second_turtle.xcor() < -280:
      second_turtle.backward(20)
    if second_turtle.xcor() > 270:
      second_turtle.backward(20)
    if second_turtle.ycor() < -260:
      second_turtle.backward(20)
    if second_turtle.ycor() > 220:
      second_turtle.backward(20)

game()
