# -*- coding:utf-8 -*-
import No40_ModulePy 
print "*" * 40
print "First Test the use of Module: "
#调用的时候直接使用模块名调用就可以
No40_ModulePy.printApple()
print "My name is %s . " %No40_ModulePy.name

print "*" * 40
print "Now we will use class and instance . "

class MyStuff(object):
	#attr 必须声明，否则在后边取thing.attr的时候会报错，但是现在还是取不到，这个我赋的值
	attr = "th"#说明构造函数中的赋值不起作用。。。
	#最后终于发现init函数没有写对，来自stackOverFlow
	#init前后不是一个下划线，而是两个连在一起的，要有两个下划线
	#这也说明 attr是可以不用声明，直接就能使用的
	def __init__ (self):
		self.attr = "I am gyt."
	def apple(self):
		print "I am a red apple!!!"

thing = MyStuff()
thing.apple()
print "thing.attr: ", thing.attr

print '*' * 40
print "We do exercise: "

class Song(object):
	
	def __init__ (self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_birth = Song(["Happy birthday to you",
					"I dont want repeat the song",
					"I will stop here"])
					
Jingle_Bells = Song(["Jingle bells jingle bells",
					 "Jingle all the way",
					 "Oh what fun it is to ride a horse"]) 

happy_birth.sing_me_a_song()
print '*' * 20
Jingle_Bells.sing_me_a_song()
