import checker
import sys
import logger

if __name__ == '__main__':
	outputToTerminal = True if "-t" in sys.argv else False 
	sys.stdout = logger.logger(outputToTerminal)
	checker = checker.checker()
	checker.main()
