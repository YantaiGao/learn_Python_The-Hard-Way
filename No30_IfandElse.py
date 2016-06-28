#-*- coding:utf-8 -*-
people = 10
cars = 40
buses = 15

#注意：无论是if 还是 elif 或者else后边都跟一个冒号，然后次行缩进4个空格（一个tab）
if cars > people:
	print "We should take the cars"
#需要注意的是：在python中 不是 else if，而是 elif!!!
elif cars < people:
	print "We should not take the cars"
else:
	print "We cannot decide"

if buses > cars:
	print "Thats too many buses"
elif buses < cars:
	print "Maybe we could take the buses"
else:
	print "We still cant decide"

if people > buses:
	print "Alright , let us take the buses."
else:
	print "Fine ,we stady at home then."