#-*- coding:utf-8-*-
print "You enter a room with two doors,which door will u choose #1 or #2 ?"

door = raw_input('>')

if(door == '1'):
	print "There is a bear eating a cake,what will U do?"
	print "1: take the cake."
	print "2: Scream at the bear."
	#""和''都是可以的
	bear =raw_input(">")
	if(bear == "1"):
		print "The bear eats your face off. Good!"
	elif(bear == "2"):
		print "The bear eats your legs off.Good!"
	else:
		print "Well ,doing %s maybe better.Bear may run away." % bear
		
elif(door == '2'):
	print "There three girl,which would U choose : "
	print "1: The girl is vary beautiful but has bad temp."
	print "2: The girl is vary rich,but urgly."
	print "3: The girl is not rich and the girl is not beautiful but the girl is good."
	girl = raw_input(">")
	if(girl=="1" or girl == "2"):
		print "You will not hadppy at last."
	else:
		print "You will have a hadppy life."

else:
	print "You fall from floor 10 and fall on knife and die.Game over!!!"