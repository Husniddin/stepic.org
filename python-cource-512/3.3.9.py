import sys
import re

# pattern = r'z\w{3}z'
pattern = r'*z.{3}z*'
for line in sys.stdin:
	line = line.rstrip()
	if re.match(pattern, line):
		print('\n--------------')
		print(line)