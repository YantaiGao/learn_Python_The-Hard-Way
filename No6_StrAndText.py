
# -*- coding:utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

#下边这两句是 %r与%s的区别 
print "I said : %r." %x 
print "I also said : '%s'." %y 

hilarious = False
joke_evalution = "Isnot that joke so funny?! %r"
print joke_evalution %hilarious

w = "This is the left side of ..."
e = " a string with a right side."
# 使用加号可以连接两个更长的字符串
print w + e

print w,e
