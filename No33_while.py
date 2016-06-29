# -*- coding:utf-8 -*-
i = 0
numbers = []

while i < 6:
	print "At the top i is %d " %i
	
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ",numbers
	print "At the bottom i is %d " %i

print "print the numbers:"

for num in numbers:
	print num,
print "\n"
	
#改进一，将while改成函数，将6变成变量

def arrIncrease(stopNum):
	i = 0
	res = []
	while i < stopNum:
		res.append(i)
		i = i+1
	return res

print "请输入终止数字：".decode('utf-8').encode('gbk')
stopInput = int(raw_input(">"))	
resArray = arrIncrease(stopInput)
print "print the res numbers:"

for nums in resArray:
	print nums,
print "\n"

#改进二，将while改成函数，将6变成变量，将增长长度也变成变量

def arrIncrease(stopNum,len):
	i = 0
	res = []
	while i < stopNum:
		res.append(i)
		i = i+len
	return res

print "请输入终止数字：".decode('utf-8').encode('gbk')
finIn = int(raw_input(">"))	
print "请输入增长长度：".decode('utf-8').encode('gbk')
lenIn = int(raw_input(">"))	

resArray1 = arrIncrease(finIn,lenIn)
print "print the res1 numbers:"

for nums in resArray1:
	print nums,
	
	
