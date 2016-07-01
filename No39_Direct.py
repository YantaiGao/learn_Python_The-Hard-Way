# -*- coding:utf-8 -*- 

#简单认识
print '*' * 40
stuff = {'name':'gyt','age':26,'height':178}

print "stuff[\'name\']: " , stuff['name']
print "stuff[\'age\']: " , stuff['age']
print "stuff[\'height\']: " , stuff['height']

#这样实现了添加
stuff[1] = "Wow"
stuff[2] = "Hello"

print stuff[1]
print stuff[2]
print "stuff : \n" 
print stuff

#direct 删除的实现!!!
del stuff[1]
del stuff[2]
print stuff
print '*' * 40

states = [
	'Oregon':'OR',
	'Florida':'FL',
	'New York':'NY',
	'California':'CA',
	'Michigan':'MI'
	
]

cities = [
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville',
]
