import os
import os.path

# print(os.getcwd())
# print(os.listdir('main'))
# print(os.path.exists('main/aelpx.txt'))

l = []

for cur_dir, dirs, files in os.walk('main'):
	# print(cur_dir)
	# print(dirs)
	# print(files)
	
	if len(files):
		for file in files:
			if file.endswith('.py'):
				l.append(cur_dir)
				break
	# print('-------------------------------------------------')
l = sorted(l)

content = '\n'.join(l)

with open('pydirs.txt', 'w') as p:
	p.write(content)
print(len(l))