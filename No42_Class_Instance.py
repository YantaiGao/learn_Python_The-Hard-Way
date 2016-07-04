# -*- coding:utf-8 -*-

#定义一个父类 空类
class Animal(object):
	pass

#子类 继承自父类
class Dog(Animal):
	#构造函数
	def __init__(self,name):
		#赋值
		self.name = name

#子类2 继承自父类		
class Cat(Animal):
	#构造函数
	def __init__(self,name):
		self.name = name

class Person(object):
	
	def __init__(self,name):
		self.name = name
		#变量
		self.pet = None
	
class Employee(Person):
	def __init__(self,name,salary):
		#使用父类的构造方法，注意格式
		super(Employee,self).__init__(name)
		self.salary = salary

class Fish(object):
	pass
	
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass
	
doudou = Dog("Doudou")

miaomi = Cat("Miaomi")

gyt = Person("Gyt")

gyt.pet = doudou

jack = Employee("Jack",12000)
jack.pet = miaomi

fish = Fish()
xiaoS = Salmon()
xiaoH = Halibut()

print doudou.name
print gyt.pet.name