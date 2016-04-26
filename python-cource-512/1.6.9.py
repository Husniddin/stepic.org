import time

class Loggable():
	def log(self, msg):
		print(str(time.ctime()) + ": " + str(msg))
		
class LoggableList(list, Loggable):
	def append(self, arg):
		super(LoggableList, self).append(arg)
		self.log(arg)

	def log(self, msg):
		super(LoggableList, self).log(msg)

l = LoggableList()
l.append(5)
l.append(6)
l.append(7)
		