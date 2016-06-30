# -*- coding:utf-8 -*-

#注意类的声明方法：

class Thing(object):
	#self是需要有的 否则报错
	def test(self,hi):
		print hi

a = Thing()
a.test("hahaha")

print "---------------------------------"

test_things = "Apple Orange Crows Telephone Light Suger"
print "There is not 10 things in that list,let's fix it."

stuff = test_things.split(' ')

more_stuff = ["Mon","Tues","Wed","Thris","Fir","Sat","Sun","MOON"]

while len(stuff)!=10:
	#注意：pop()方法是从后往前出，先出最后一个
	next = more_stuff.pop()
	print "Adding ", next
	#append()方法是增加
	stuff.append(next)
	print "There are %d elements in list " %len(stuff)
	
print "Here we go: ",stuff

#注意：下标从0开始！！！
print stuff[1]
#-1是最后一个
print "stuff[-1] == ",stuff[-1]
print "stuff[-2] == ",stuff[-2]

print stuff.pop()
