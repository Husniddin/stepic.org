s = input()
a = input()
b = input()

i = 0

if a not in s:
	i = 0
elif a in b:
	i = 'Impossible'
elif a in s:
	while True:
		i += 1
		s = s.replace(a, b)
		if a not in s:
			break

print(i)






print(s.replace(a, b))