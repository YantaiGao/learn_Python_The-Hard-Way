# -*- coding:utf-8 -*-
import random
#从urllib中导入urlopen
from urllib import urlopen
import sys

WORD_URL = "http://learnpythonthehardway.org/words.txt"

#声明列表
WORDS = []

PHREASE = {
	"Class %%% (%%%)":"declare a class and father class is %%%",
	"Class %%%(object):\n\t def __init__(self,***)":"declare a class with a init method",
	"Class %%%(object):\n\t def ***(self,***)":"declare a class with a method called ***",
	"*** = %%%()":"declare a instance of class %%%",
	"***.***(@@@)":"call method ***",
	"***.***=\'***\'":"set the value of instance *** "		
}

PHREASE_FIRST = False
#判断是不是有两个运行参数，而且第二个为eng的话，置flag为true
if(len(sys.argv)==2 and sys.argv[1]=="english"):
	PHREASE_FIRST = True

print "PHREASE_FIRST:",PHREASE_FIRST

#从网页下载到列表，由于网页网址已经404 ，我们使用模拟的方法

#for word in urlopen(WORD_URL).readline():
#	WORDS.append(word)

WORDS.append("Word1")
WORDS.append("Word2")
WORDS.append("Word3")
WORDS.append("Word4")
WORDS.append("Word5")
WORDS.append("Word6")
#[:]的作用？？？
for sentence in WORDS:
	res = sentence[:]
	print res

#ctrl+d退出 在cmd中ctrl+d是不能退出的，ctrl+c才能强制退出
try:
	while True:
		#keys()方法，返回字典的一个list
		indexKeys = PHREASE.keys()
		#random.shuffle()将列表随机打乱，洗牌
		random.shuffle(indexKeys)
		
		for indexKey in indexKeys:
			val = PHREASE[indexKey]
			#注意这种赋值方法
			question,answer = indexKey,val
			#若是带有参数，则将答案和问题反过来
			if PHREASE_FIRST:
				question,answer = val,indexKey
			print question
			
			raw_input(">")
			print "Answer: %s\n\n" %answer
		
except EOFError:
	print "\n Bye"