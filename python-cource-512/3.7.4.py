from xml.etree import ElementTree

cubs = input()

tree = ElementTree.fromstring(cubs)
# tree = ElementTree.parse(cubs)
# tree = ElementTree.parse('example.xml')

# print(tree)
# exit()

# root = tree.getroot()

s = 1

r = 0
g = 0
b = 0

# print(tree.tag, tree.attrib, tree.attrib['color'])

if tree.attrib['color'] == 'red':
	r += s
elif tree.attrib['color'] == 'green':
	g += s
elif tree.attrib['color'] == 'blue':
	b += s

def getChild(root, s):
	
	global r, g, b

	for child in root:
		# print(child.tag, child.attrib, child.attrib['color'])
		
		if child.attrib['color'] == 'red':
			r += s
		elif child.attrib['color'] == 'green':
			g += s
		elif child.attrib['color'] == 'blue':
			b += s

		if len(child) >=1:
			getChild(child, s+1)

getChild(tree, s+1)

print(r, g, b)
