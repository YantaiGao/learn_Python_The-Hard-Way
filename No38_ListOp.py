# -*- coding:utf-8 -*-

#注意类的声明方法：

class Thing(object):
	#self是需要有的 否则报错
	def test(self,hi):
		print hi

a = Thing()
a.test("hahaha")