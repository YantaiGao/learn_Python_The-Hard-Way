# -*- coding:utf-8 -*-
from nose.tools import *
from Model.game import Room

def test_Room():
	#首先 new一个对象，然后检查是不是正确
	gold = Room("GoldRoom","A room full of gold.")
	assert_equal(gold.name,"GoldRoom")
	assert_equal(gold.description,"A room full of gold.")
	assert_equal(gold.paths,[])

