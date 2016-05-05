import json

js = json.loads(input())

cls = {}

childs = []

def getChildsCount(cl, js):
	global childs
	# i = 0
	count = 0
	for j in js:
		# i += 1
		# print('i - ' + str(i))

		if cl in j['parents'] and j['name'] not in childs:
			child = j['name']
			childs.append(child)
			count += 1
			
			# print("child - " + child)
			# if child in cls:
			# 	count += cls[child]
			# 	continue

			c1 = getChildsCount(child, js)
			count += c1

	return count


for j in js:

	cl = j['name']
	# cls[cl] = 1
	
	count = 0
	# print(cl)
	count += getChildsCount(cl, js)
	# print(count)
	# print('---------------------------')

	cls[cl] = count

	print(childs)
	childs = []

# print(cls)

for key, value in sorted(cls.items()):
	print("{} : {}".format(key, value+1))

# def getParentParentsCount(parents, js):
	
# 	count = 0

# 	for parent in parents:
# 		if parent in cls:
# 			count += cls[parent]
# 			continue
		
# 		for j in js:
# 			if j['name'] == parent:
# 				if len(j['parents']) == 0:
# 					continue
				
# 				count += len(j['parents'])
# 				c1 = getParentParentsCount(j['parents'], js)
# 				count += c1

# 	return count


# cls = {}

# for j in js:

# 	cl = j['name']
# 	cls[cl] = len(j['parents'])
	
# 	if cls[cl] == 0:
# 		continue

# 	count = getParentParentsCount(j['parents'], js)

# 	cls[cl] += count

# print (cls)
# for key, value in sorted(cls.items()):
# 	print("{} : {}".format(key, value))
# print ( sorted(cls.items()) )