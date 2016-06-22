def print_o():
	print "there is no args"

def print_one(arg1):
	print "arg1 == %s " %(arg1)

def print_two(arg1,arg2):
	print "arg1 = %s ,arg2 = %s " %(arg1,arg2)
	
def print_two_(*args):
	arg1,arg2 = args
	print "arg1 = %r ,arg2 = %r" %(arg1,arg2)
	
print_o()
print_one("gyt")
print_two("gyt","th")
print_two_("th","gyt")