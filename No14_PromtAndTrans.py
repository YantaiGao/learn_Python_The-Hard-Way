from sys import argv

script,user_name = argv
prompt = '>'

print "Hi %s,I am the %s script" % (user_name,script)
print " I would like to ask U a few questions."

print "Do you like me %s?" %(user_name)
likes = raw_input(prompt)

print "where do you live %s?" %(user_name)
lives = raw_input(prompt)

print "what kind of conputer do u have ,%s" %(user_name)
com = raw_input(prompt)

print """

Alright,so you are said %r about like me .
You live in %s .I am not sure where it is.
And You have a %s computer! Nice!

""" %(likes,lives,com)