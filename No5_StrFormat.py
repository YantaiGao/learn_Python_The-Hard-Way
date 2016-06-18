# -*- coding:utf-8 -*-
my_name = "gyt"
my_age = 26
my_height = 178	#cm
my_weight = 62 #kg
my_tooth = "white"
my_eyes = "black"
my_hire = "Black" 

print "Now I will introduce myself:"
# 注意：
# 1：str和后边的 %变量名之间没有 逗号
# 2：前边str中含有 %d 或者 %s 后边没有，后边只有一个 % 即可
print "my name is %s" % my_name
print "I am %d years old" % my_age 
print "I am %d cm high" %my_height
print "my weight is %d kg " %my_weight
print "my tooth are %s" %my_tooth ,"in color."
print "my eyes are %s" %my_eyes
print "str1 -","-> str2"

print "if I add %d , %d , %d then I will get %d" %(my_age,my_height,my_weight,my_age+my_height+my_weight)
