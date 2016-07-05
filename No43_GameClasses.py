# -*- coding:utf-8 -*-


#场景父类
class Scene(object):
	def enter(self):
		pass

#引擎类
class Engin(object):
	def __init__(self,scene_map):
		pass
	def play(self):
		pass

#地图类
class Map(object):
	def __init__(self,start_scene):
		pass
	def open_scene(self):
		pass
	def next_scene(self,scene_name):
		pass
	

#中央走廊
class CentralRoad(Scene):
	def enter(self):
		pass

#武器库场景
class WeaponArmory(Scene):
	def enter(self):
		pass

#主控制室
class MainContralRoom(Scene):
	def enter(self):
		pass
	
#逃生舱
class EscapeRoom(Scene):
	def enter(self):
		pass
	
#死亡场景
class DeathScene(Scene):
	def enter(self):
		pass

a_map = Map(CentralRoad)
a_game = Engin(a_map)
a_game.play()