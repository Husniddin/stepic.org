f = open('dataset_24465_4.txt')
l = []

for line in f:
	l.append(line.rstrip())

f.close()
l.reverse()
content = '\n'.join(l)

n = open('file2.txt', 'w')
n.write(content)
n.close()


# 2 method
# with open('file1.txt', 'r') as f, open('file2.txt', 'w') as n:
# 	a = reversed(f.read())
# 	for x in a:
# 		print(x)