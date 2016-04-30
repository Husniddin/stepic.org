import itertools

def primes():
	n = 2
	yield n

	n = 3
	yield n

	while True:
		
		n += 2

		next = False

		for x in range(3, n, 2):
			
			if n%x == 0:
				next = True
				break

			elif n//x < 3:
				break

		if next:
			continue

		yield n

# n = 5
# for x in range(5, n, 2):
# 	print(x)
# print(n)
# exit()

print(list(itertools.takewhile(lambda x : x <= 31, primes())))