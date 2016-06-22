from sys import argv

script,filename = argv

print "We are going to erease %s " %(filename)

print "If U dont want do it hit CTRL + C "
print "If U want do hit enter."
raw_input("?")

print "Open the file ..."

target = open(filename,'w')

print "truncate the file ,goodbye."
#target.truncate()

print "Now I will ask U to typein 3 line:"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I will write the three line into %s" %(filename)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally we close the file ..."

target.close()
