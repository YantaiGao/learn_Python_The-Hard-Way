#-*-coding:utf-8-*-
the_count = [1,2,3,4,5]
fruits = ['apple','orianges','pears']
change = [1,'peoples',2,'boys',3,'girls']

#遍历数组
for num in the_count:
	print "This is count : %d " % num

for fruit in fruits:
	print "A fruit of type : %s " % fruit
	
for i in change:
	print "I got : %r " %i
#声明一个数组
elements = []

for i in range(0,6):
	print "Adding %d to the list" %i
	#注意添加 使用append
	elements.append(i)

for i in elements:
	print "Element is %d " %i