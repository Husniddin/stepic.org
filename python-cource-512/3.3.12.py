import sys
import re

pattern = r"human"

for string in sys.stdin:
	string = string.rstrip()
	print(re.sub(pattern, 'computer', string))