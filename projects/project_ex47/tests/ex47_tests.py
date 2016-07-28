# -*- coding:utf-8 -*-
from nose.tools import *
from Model.game import Room

def test_Room():
	#首先 new一个对象，然后检查是不是正确
	gold = Room("GoldRoom","A room full of gold.")
	#assert_equal函数，保证函数变量与预期相符
	assert_equal(gold.name,"GoldRoom")
	assert_equal(gold.description,"A room full of gold.")
	assert_equal(gold.paths,{})

def test_room_paths():
	
	centerroom = Room("Center","The room in center.")
	northroom = Room("North","The room in north.")
	southroom = Room("South","The room in south.")
	
	centerroom.add_paths({"north":northroom,"south":southroom})
	
	assert_equal(centerroom.go("north"),northroom)
	assert_equal(centerroom.go("south"),southroom)
	
	
	