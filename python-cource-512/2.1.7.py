t = int(input())
print('t = ' + str(t))
classes = {}

for x in range(t):

	string = input().split(' : ')
	child = string[:1]
	string_parents = string[1:]

	if child[0] not in classes:
		classes[child[0]] = []

	if len(string_parents) > 0:
		
		parents = string_parents[0].split(" ")
		classes[child[0]].extend(parents)

		for parent in parents:
			if parent in classes:
				classes[child[0]].extend(classes[parent])

	for k in classes:
		if child[0] in classes[k]:
			classes[k].extend(classes[child[0]])

print(classes)

r = int(input())
print('r = ' + str(r))

# excs = []
excs = {}
nw = []
# for x in range(r):
# 	exception = input()
# 	excs.append(exception)

for x in range(r):
	exception = input()

	s = False

	for exc in excs:
		if exception in excs[exc]:
			nw.append(exception)
			s = True
			break

	if s:
		continue		

	ch_s = []
	for ch in classes:
		if exception in classes[ch]:
			ch_s.append(ch)
	
	excs[exception] = ch_s

print('excs = ')
print(excs)
print('nw = ')
print(nw)

for n in nw:
	print(n)