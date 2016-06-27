#-*- coding:utf-8 -*-

people = 30
cats = 35
dogs = 15

if people < cats:
	print "people < cats : %d , %d" %(people,cats)
	print "Too many cats !!!"

if people > cats:
	print "people and cats: %d , %d" %(people,cats)
	print "Not many cats."

if people < dogs:
	print "people < dogs: %d , %d" %(people,dogs)
	print "Too many dogs."

if people >dogs:
	print "people and dogs: %d , %d" %(people,dogs)
	print "Not many dogs."

dogs += 15

if people >= dogs:
	print "People >= dogs"
	
if people <= dogs:
	print "People <= dogs"
	
if people == dogs:
	print "People are dogs"