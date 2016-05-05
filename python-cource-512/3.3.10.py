import sys
import re

pattern = r"\\"

for string in sys.stdin:
	string = string.rstrip()

	if re.match(pattern, string) != None:
		print('\n-----------')
		print(string)