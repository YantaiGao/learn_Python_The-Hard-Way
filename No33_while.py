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
	print num
	
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
