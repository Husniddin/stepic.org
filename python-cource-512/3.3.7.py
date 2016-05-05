import sys

for line in sys.stdin:
	line = line.rstrip()
	if line.count('cat') >= 2:
		print(line)