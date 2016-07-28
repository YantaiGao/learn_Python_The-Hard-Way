# -*- coding:utf-8 -*-
class Room(object):
	
	#构造函数 有两个参数
	def __init__(self,name,description):
		self.name = name
		self.description = description
		self.paths = []
		
	#go()方法，取paths的指定key的值
	def go(self,direction):
		#None安全获取
		return self.paths.get(direction,None)
		
	def add_paths(self,paths):
		#update方法，将字典的k-v对添加到字典中
		self.paths.update(paths)