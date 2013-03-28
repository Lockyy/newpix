class logger(object):
	def __init__(self):
		self.logFile = "log.txt"

	def write(self, message):
		with open(self.logFile, "a") as output:
			output.write(message)
