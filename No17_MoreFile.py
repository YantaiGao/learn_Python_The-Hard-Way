from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copy from %s to %s" %(from_file,to_file)

#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long " %len(indata)
print "Does the outfile exist? %s" %exists(to_file)
print "Ready,print ctrl+c to abort and enter to continue"
raw_input()

outFile = open(to_file,'w')
outFile.write(indata)
print "All Right,all done."

outFile.close()


