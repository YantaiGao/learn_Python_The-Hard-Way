#-*- coding:utf-8 -*-
def break_words(sentence):
	"""This function will break words ..."""
	words = sentence.split(' ')
	return words

#sorted排序的时候 先排大写，再排小写，大写排在小写的前边
def sort_words(words):
	"""Sort the words"""
	return sorted(words)	

def print_first_words(words):
	"""print the first word"""
	word = words.pop(0)
	return word
	
def print_last_word(words):
	"""print the last word"""
	word = words.pop(-1)
	return word

def sort_sentence(sentence):
	"""Take a full sentence and return the sorted words"""
	words = break_words(sentence)
	words = sort_words(words)
	return words
	
def print_first_and_last(sentence):
	"""Print the first and last sentence"""
	words = break_words(sentence)
	print_first_words(words)
	#print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Print the first and last sentence"""
	words = sort_sentence(sentence)
	print_first_words(words)
	print_last_word(words)
	
sen = "hello goodmorning everyone I am gyt and she is th A Z"

wordArr = break_words(sen)

print wordArr

soreArr = sort_words(wordArr)

print soreArr

print print_first_words(wordArr)
print print_last_word(wordArr)

print sort_sentence(sen)
#为啥最后这俩返回none
print "------"
print print_first_and_last(sen)
print "------"
print print_first_and_last_sorted(sen)

