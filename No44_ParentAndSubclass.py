# -*- coding:utf-8 -*-

#隐式继承

class Parent(object):
	def implicit(self):
		print "Parent Implicit()"
#继承自Parent类
class Child(Parent):
	pass
	
parent = Parent()
child = Child()

parent.implicit()
child.implicit()

print "*" * 40

#显示覆盖
class Parent1(object):
	def override(self):
		print "Parent1 override():"

class Child1(Parent1):
	def override(self):
		print "Child1 override():"
		
parent1 = Parent1()
child1 = Child1()

parent1.override()
child1.override()

print "*" * 40

#部分覆盖
class Parent2(object):
	def alter(self):
		print "Parent2 alter():"

class Child2(Parent2):
	def alter(self):
		print "Child2 before:"
		super(Child2,self).alter()
		print "Child2 after:"
		
parent2 = Parent2()
child2 = Child2()

parent2.alter()
child2.alter()

print "*" * 40

#继承使用合成也就是组合替代

class Other(object):
	def implic(self):
		print "Other implic():"
	def overrid(self):
		print "Other overrid():"
	def alter(self):
		print "Other alter():"

class Child3(object):
	
	#通过内置一个对象来避免使用继承
	def __init__(self):
		self.other = Other()
	
	def implic(self):
		self.other.implic()
	
	def overrid(self):
		print "Child3 overrid()"
		
	
	def alter(self):
		print "Before alter: "
		self.other.alter()
		print "After alter: "
child3 = Child3()
child3.implic()
child3.overrid()
child3.alter()
