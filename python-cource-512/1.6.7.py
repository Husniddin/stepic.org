t = int(input())
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

r = int(input())

for x in range(r):
	
	rr = input().split(" ")
	
	if rr[1] in classes and rr[0] in classes[rr[1]]:
		print("Yes")
	elif rr[0] == rr[1]:
		print("Yes")
	else:
		print("No")