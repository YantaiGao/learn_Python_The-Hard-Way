# -*- coding:utf-8 -*-
def gold_room():
	print "Congratulations!!! You enter a room full of gold!!! And How much do you want to take away?"
	
	next = raw_input(">")
	#这种判断数字的方式简直弱智 且 不正确，我们只是随便使用下
	if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next:
		how = int(next)
	else:
		dead("You should learn to type in nums.")
	
	if(how <= 50):
		print "Nice! You win."
		exit(0)
	else:
		dead("You are too greedy and killed by hurry gold.")
	

def bear_room():
	print "You enter a room with a bear!!!"
	print "The bear is in front another door and it has a apple in hand."
	print "How to move the bear?"
	bear_mov = False
	while True:
		next = raw_input(">")
		if next == "take apple":
			dead("You take the bear's food and it eat your face.")
		elif next == "beat bear" and not bear_mov:
			print "The bear moved to you ,quickly run"
			bear_mov = True
		elif next == "scare bear" and bear_mov:
			dead("You make bear cazry and killed by it") 
		elif next == "open door" and bear_mov:
			gold_room()
		else:
			print "Sorry ,wrong way to get out."
		

def crazy_room():
	print "You enter a crazy room!!!"
	print "You will eat your head or you feet?"
	next = raw_input(">")
	if("feet" in next):
		print "Thank the god!!! You have another choice to choose the door."
		start()
	elif("head" in next):
		dead("You dont have your head.")
	else:
		crazy_room()
	
def dead(why):
	print why , " Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your left and right."
	print "Which one would You like to take."
	
	next = raw_input(">")
	
	if next == "left":
		bear_room()
	elif next == "right":
		crazy_room()
	else:
		dead("You didn't choose the door,because you dont have food.")

#开始游戏
start()