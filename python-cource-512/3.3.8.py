import sys
import re

# pattern = r"([?!\"\s]?(\bcat\b))"
# pattern = r"([?!\"\s]?(\bcat\b))|(\bcat\b)"
# pattern = r"([?!\"\s]?\bcat\b)|(\bcat\b)"
pattern = r"[\s]{1}cat\b"
# string = "acc"

for string in sys.stdin:
	string = string.rstrip()

	if re.match(pattern, string):
		print('\n-----------')
		print(string)