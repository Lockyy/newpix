import sys

class logger(object):
	def __init__(self, outputToTerminal):
		self.outputToTerminal = outputToTerminal
		self.terminal = sys.stdout
		self.logFile = "log.txt"

	def write(self, message):
		if self.outputToTerminal:
			self.terminal.write(message)

		with open(self.logFile, "a") as output:
			output.write(message)