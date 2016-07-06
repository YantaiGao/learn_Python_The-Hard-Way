# -*- coding:utf-8 -*-

#仔细研究游戏流程调用，很有意思，没有那么简单的一个游戏！！！

#基本导入
from sys import argv
from random import randint

#场景父类
class Scene(object):
	def enter(self):
		print "The scene is not yet configed.subclass will implement it."
		exit(1)
#引擎类
class Engin(object):

	def __init__(self,scene_map):
		self.scene_map = scene_map
		
	def play(self):
		#作用：获取一个场景对象实例
		curren_scene = self.scene_map.open_scene()
		
		while True:
			print "-" * 40
			next_scene_name = curren_scene.enter()
			#作用：根据返回值获取一个新的场景对象
			curren_scene = self.scene_map.next_scene(next_scene_name)

#场景
#中央走廊
class CentralRoad(Scene):
	def enter(self):
		print "You are in The CentralRoad."
		print "And you are going to WeaponArmory,"
		print "But a big animal is before you."
		print "What will U do? "
		print "shoot! or dodge! or tell a joke"
		
		action = raw_input('>')
		
		if action == "shoot!":
			print "Sorry ... "
			return "death_scene"
		elif action == "dodge!":
			print "Sorry ... "
			return "death_scene"
		elif action == "tell a joke":
			print "Congratulations!!!"
			return "weapon_armory"
		else:
			print "Dose not compute!"
			return "central_road"

#武器库场景
class WeaponArmory(Scene):
	def enter(self):
		print "You are in the WeaponArmory."
		print "Guess the password of the weapon."
		print "The code is 3 digits."
		#随机产生3位随机数
		code = "%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
		
		#游戏作弊
		print "Promotion: " , code
		
		guess = raw_input("[KeyPad]>>>")
		guess_time = 0
		
		while guess != code and guess_time < 10:
			print "WRONG!!!"
			guess_time += 1
			guess = raw_input("[KeyPad]>>>")
		
		if guess == code:
			print "Congratulations!!!"
			return "mainContral_room"
		else:
			print "Sorry ... "
			return "death_scene"

#主控制室
class MainContralRoom(Scene):
	def enter(self):
		print "You are in the MainContralRoom."
		print "What will you treat the bomb?"
		print "throw or slowly place"
		
		action = raw_input('>')
		
		if action == "throw":
			print "Sorry ... "
			return "death_scene"
		elif action == "slowly place":
			print "Congratulations!!!"
			return "escape_room"
		else:
			print "Dose not compute!"
			return "mainContral_room"
	
#逃生舱
class EscapeRoom(Scene):
	def enter(self):
		print "You are in the EscapeRoom."
		print "5 door only one can live."
		print "Choose one,1 or 2 or 3 or 4 or 5."
		good_num = randint(1,5)
		#游戏作弊
		print "Num : ",good_num
		guess = raw_input('[Door_Num]>>>')
		
		if int(guess) != good_num:
			print "Sorry ... "
			return "death_scene"
		else:
			print "Congratulations!!!"
			#没有finish对应场景将报错，加一个就好了
			return "finished"
	
#死亡场景
class DeathScene(Scene):
	deaths = ["You died! ",
			  "Such a loser",
			  "You mom will be proud of you ... ",
			  "Try again,Wish You have a better score!!!"]
	def enter(self):
		#注意这个随机取法
		print DeathScene.deaths[randint(0,len(self.deaths)-1)]
		exit(1)
			
#地图类
class Map(object):
	scenes = {"central_road":CentralRoad(),
			  "weapon_armory":WeaponArmory(),
			  "mainContral_room":MainContralRoom(),
			  "escape_room":EscapeRoom(),
			  "death_scene":DeathScene()
			  }
	def __init__(self,start_scene):
		self.start_scene = start_scene
	def open_scene(self):
		return self.next_scene(self.start_scene)
	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
	
#开始游戏
a_map = Map('central_road')
a_game = Engin(a_map)
a_game.play()
