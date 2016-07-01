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
	def _init_(self):
		self.attr = "I am gyt."
	def apple(self):
		print "I am a red apple!!!"

thing = MyStuff()
thing.apple()
print "thing.attr: ",thing.attr
		