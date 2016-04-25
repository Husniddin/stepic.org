class Buffer(object):

	def __init__(self):
		self.integers = []

	def add(self, *a):
		self.integers.extend(a)
		while len(self.integers) >= 5:
			print(sum(self.integers[:5]))
			self.integers = self.integers[5:]

	def get_current_part(self):
		return self.integers