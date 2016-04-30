class multifilter():

	def judge_half(pos, neg):
		return pos >= neg

	def judge_any(pos, neg):
		return pos >= 1

	def judge_all(pos, neg):
		return neg == 0

	def __init__(self, iterable, *funcs, judge=judge_any):
		self.iterable = iter(iterable)
		self.funcs = funcs
		self.judge = judge

	def __iter__(self):
		return self

	def __next__(self):

		while True:
			self.pos = 0
			self.neg = 0
			
			n = next(self.iterable);
			for func in self.funcs:
				if func(n):
					self.pos += 1
				else:
					self.neg += 1
			if self.judge(self.pos, self.neg):
				return n 

# m = multifilter([1,2,3], 'a', 'b', 'c')

def mul2(x):
	return x % 2 == 0

def mul3(x):
	return x % 3 == 0

def mul5(x):
	return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# t = multifilter(a, mul2, mul3, mul5)
# print(next(t))
# print(next(t))
# print(next(t))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))