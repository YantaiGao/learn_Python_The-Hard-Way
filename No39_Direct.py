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

#注意：使用中括号是不对的
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'New York':'NY',
	'California':'CA',
	'Michigan':'MI'
}

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville',
}
# add some city
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '*' * 40
print "NY state has: ",cities['NY']
print "OR state has: ",cities['OR']

#print some state
print '*' * 40
print "Michigan upcase: ",states['Michigan']
print "Florida upcase: ",states['Florida']

#关联查询
print '*' * 40
print "Michigan has : ",cities[states['Michigan']]
print "Florida has : ",cities[states['Florida']]

#遍历 k v
print '*' * 40
for astr,up in states.items():
	print "%s Up is %s ." %(astr,up)

print '*' * 40
for sta,city in cities.items():
	print "State %s has %s ." %(sta,city)

#安全获取	
print '*' * 40
state = states.get('Texas',None)

if not state:
	print "Sorry ,no Texas. "

#获取默认值
city = cities.get('TX','Does Not Exist')
print "The　city for the state \'TX\' is : %s" %city
	