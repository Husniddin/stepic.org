s = input()
t = input()

i = 0

if t in s:
	while True:
		i += 1
		index = s.find(t)
		s = s[index+1:]
		if t not in s:
			break


print(i)