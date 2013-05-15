import checker
import sys
import logger
import argparse
try:
	import pygame
except:
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Capture the updating xkcd comic, \"Time\". xkcd.com/1190")

	helpMessages = {}
	helpMessages["outputToTerminal"] = "Turns console output on."
	helpMessages["logFileLogging"] = "Turns logging off."
	helpMessages["gitOutput"] = "Turns output to xkcdTimeImages folder off."
	helpMessages["sound"] = "Turns sound on. Will beep whenever an image is found."

	parser.add_argument('-t', action = "store_true", dest = "outputToTerminal", default = False, help = helpMessages["outputToTerminal"])
	parser.add_argument('-l', action = "store_false", dest = "logFileLogging", default = True, help = helpMessages["logFileLogging"])
	parser.add_argument('-g', action = "store_false", dest = "gitOutput", default = True, help = helpMessages["gitOutput"])
	parser.add_argument('-s', action = "store_true", dest = "sound", default = False, help = helpMessages["sound"])

	settings = parser.parse_args()

	if not "pygame" in sys.modules:
		settings.sound = False

	sys.stdout = logger.logger(settings.outputToTerminal, settings.logFileLogging)
	checker = checker.checker(settings.gitOutput, settings.sound)
	checker.main()
