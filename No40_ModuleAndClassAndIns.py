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
	def _init_(self):
		self.attr = "I am gyt."
	def apple(self):
		print "I am a red apple!!!"

thing = MyStuff()
thing.apple()
print "thing.attr: ", thing.attr

print '*' * 40
print "We do exercise: "
		