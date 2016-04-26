class ExtendedStack(list):
	def sum(self):
		top1 = self.pop()
		top2 = self.pop()
		r = top1 + top2
		self.append(r)
	def sub(self):
		top1 = self.pop()
		top2 = self.pop()
		r = top1 - top2
		self.append(r)
	def mul(self):
		top1 = self.pop()
		top2 = self.pop()
		r = top1 * top2
		self.append(r)
	def div(self):
		top1 = self.pop()
		top2 = self.pop()
		r = top1 // top2
		self.append(r)
		