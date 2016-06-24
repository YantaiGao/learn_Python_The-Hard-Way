#-*- coding:utf-8 -*-

#有返回值的函数
def add(a,b):
	print "add %d , %d " %(a,b)
	return a + b
def sub(a,b):
	print "sub %d ,%d " %(a,b)
	return a - b
def mul(a,b):
	print "mul %d ,%d " %(a,b)
	return a * b
def div(a,b):
	print "div %d ,%d " %(a,b)
	return a / b

print "Let us do some exercise: "

age = add(20,6)
height = sub(180,2)
weight = mul(63,2)
iq = div(1000,5)

print "Age: %d ,height: %d ,weight: %d ,iq: %d" %(age,height,weight,iq)

print "a puzzle"
#一个嵌套的算术式
what = add(age,sub(height,mul(weight,div(iq,2))))

print "what is %d " %(what)
