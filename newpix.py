import checker
import sys
import logger

if __name__ == '__main__':
	sys.stdout = logger.logger()
	checker = checker.checker()
	checker.main()
