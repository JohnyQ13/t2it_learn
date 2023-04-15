# BINGO revers
import sys
filename = sys.argv[0]
# open file to read (option 'r')
f = open(filename, 'r') # file in 'file descriptor'
lines = f.readlines()# read to lines
f.close() # close file
for line in reversed(lines): # every lines in file
	print(line, end='')
#END revers
