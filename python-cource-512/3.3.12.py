import sys
import re

pattern = r"human"

for string in sys.stdin:
	print('\n-----------------')
	string = string.rstrip()
	print(re.sub(pattern, 'computer', string))