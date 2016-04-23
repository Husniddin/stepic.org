ns_s = [{
	'name': 'global',
	'parent': None,
	'vars': [],
}]

ns_indexes = {'global': 0}

def get_name(namespace, var):
	index = ns_indexes[namespace]
	d = ns_s[index]
	if var in d['vars']:
		print(namespace)
	elif namespace == 'global':
		print('None')
	else:
		get_name(d['parent'], var)

number = int(input())

for x in range(number):
	command, namespace, mix = input().split(' ')

	if command=='create':
		l=len(ns_indexes)
		ns_indexes[namespace]=l
		ns_s.append({
			'name':namespace,
			'parent':mix,
			'vars':[]
		})
	elif command=='add':
		index = ns_indexes[namespace]
		ns_s[index]['vars'].append(mix)
	elif command=='get':
		name = get_name(namespace, mix)