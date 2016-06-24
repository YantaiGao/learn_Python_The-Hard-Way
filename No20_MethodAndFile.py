# -*- coding:utf-8 -*-
from sys import argv
script,input_file = argv

def print_all(f):
	print f.read()
	
#f.seek(0)回到文件的开始
def rewind(f):
	f.seek(0)

def print_aline(linecount,f):
	print linecount,f.readline()
	
#打开输入文件
current_file = open(input_file)

print "First print the whole file:"
print_all(current_file)

#指向文件流的指定位置
print "Now rewind: "
rewind(current_file)

print "print line by line:"

count_line = 1
print_aline(count_line,current_file)

count_line += 1
print_aline(count_line,current_file)

count_line = count_line + 1
print_aline(count_line,current_file)




