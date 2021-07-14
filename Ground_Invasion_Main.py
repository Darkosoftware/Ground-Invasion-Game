import turtle
import os
import math
import random
import time

window = turtle.Screen()
window.bgcolor("black")
window.title("Ground Invasion")
window.bgpic("background1.gif")

window.tracer(0)

turtle.register_shape("Player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("fire.gif")
turtle.register_shape("crater.gif")

window_border = turtle.Turtle()
window_border.speed(0)
window_border.color("white")
window_border.penup()
window_border.setposition(-300,-300)
window_border.pendown()
window_border.pensize(3)
for side in range(4):
	window_border.fd(600)
	window_border.lt(90)
window_border.hideturtle()

score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.setposition(-290,278)
scorestring = "Score: {}".format(score)
score_display.write(scorestring, False, align="left", font=("Arial", 14,"normal"))
score_display.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("Player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0

numenemies = 7
enemies = []
for i in range(numenemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("green")
	enemy.shape("enemy.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,250)
	y = random.randint(100,260)
	enemy.setposition(x,y)
	enemy.shapesize(8,8)
enemyspeed = 0.35

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("fire.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.3)
bullet.hideturtle()

bulletspeed = 2.2

bulletstate = "ready"

crater = turtle.Turtle()
crater.color("green")
crater.shape("crater.gif")
crater.penup()
crater.speed(0)
crater.setheading(90)
crater.shapesize(1,1)
crater.hideturtle()
craterstate = "ready"

explosion = turtle.Turtle()
explosion.color("red")
explosion.shape("square")
explosion.penup()
explosion.speed(0)
explosion.setheading(90)
explosion.shapesize(1.5,1.5)
explosion.hideturtle()
explosionstate = "ready"

timer = 0
timer_display = turtle.Turtle()
timer_display.speed(0)
timer_display.color("white")
timer_display.penup()
timer_display.setposition(205,278)
timerstring = "Timer: {}".format(timer)
timer_display.write(timerstring, False, align="left", font=("Arial", 14,"normal"))
timer_display.hideturtle()
#create a time keeper This is my code!
gameover = 0
gameover_display = turtle.Turtle()
gameover_display.speed(0)
gameover_display.color("red")
gameover_display.penup()
gameover_display.setposition(-120,-60)
gameoverstring = "GAME OVER\nFinal Score: {}\nFinal Time: {}".format(score, timer)
gameover_display.write(gameoverstring, False, align="left", font=("Arial Black", 25,"normal"))
gameover_display.hideturtle()

def move_left():
	player.speed = -1
def move_right():
	player.speed = 1
def move_stop_left():
	player.speed = 0
def move_stop_right():
	player.speed = 0
def move_player():
	x = player.xcor()
	x += player.speed
	
	if x < -280:
		x = -280
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 18
		bullet.setposition(x,y)
		bullet.showturtle()
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 20:
		return True
	else:
		return False

def craters():
	global craterstate
	if craterstate == "ready":
		craterstate = "crater"
		x = enemy.xcor()
		y = enemy.ycor()
		crater.setposition(x,y)
		crater.showturtle()
def explode():
	global explosionstate
	if explosionstate == "ready":
		explosionstate = "explode"
		x = enemy.xcor()
		y = enemy.ycor()
		explosion.setposition(x,y)
		explosion.showturtle()
def notexplode():
	global explosionstate
	if explosionstate == "explode":
		explosionstate = "ready"
		x = 0
		y = 0
		explosion.setposition(x,y)
		explosion.showturtle()

window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeyrelease(move_stop_left, "Left")
window.onkeyrelease(move_stop_right, "Right")
window.onkeypress(fire_bullet, "space")

while True:
	window.update()
	move_player()
	gameover_display.clear()
	timer = int(time.process_time())
	timerstring = "Time: {}".format(timer)
	timer_display.clear()
	timer_display.write(timerstring, False, align="left", font=("Arial", 14,"normal"))
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		if enemy.ycor() < -275:
			score -= 3
			scorestring = "Score: {}".format(score)
			score_display.clear()
			score_display.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
			for e in enemies:
				x = random.randint(-200,250)
				y = random.randint(100,260)
				enemy.setposition(x,y)
		if isCollision(bullet,enemy):
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)
			craterstate == "crater"
			craters()
			craterstate = "ready"
			x = random.randint(-220,260)
			y = random.randint(80,260)
			enemy.setposition(x,y)
			score += 5
			scorestring = "Score: {}".format(score)
			score_display.clear()
			score_display.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("GAME OVER")
			break	
  if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"
	if isCollision(player, enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("GAME OVER")
		gameoverstring = "GAME OVER\nFinal Score: {}\nFinal Time: {}".format(score, timer)
		gameover_display.clear()
		gameover_display.write(gameoverstring, False, align="left", font=("Arial Black", 25,"normal"))
		input("Press enter to close.")
    
#Copyright 2021. This is copyrighted by Darkosoftware. It can be used for non-commercial purposes only. Any other uses must have permission of the author.   
