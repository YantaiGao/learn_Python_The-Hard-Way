#-*- coding:utf-8 -*-

print "Let us practice everything!!!"

print "转义字符: ".decode('utf-8').encode('gbk'), " \n "

print "You\'d know \'bout escape with \\ that \\n is a new line \n and \\t a \t tab"

poem = """
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
"""

print "------"
print poem.decode('utf-8').encode('gbk')
print "------"

five = 10 - 3 + 8 - 9 -1

print "This should be %d " %five

#一个函数可以有多个返回值
def method(start):
	j_b = start * 500
	jars = j_b /1000
	c = jars /100
	return j_b,jars,c


start = 10000

beans,mk,lucy = method(start)

print "the res is %d , %d , %d " %(beans,mk,lucy)

print "else the res is : %d ,%d , %d" % method(start)
