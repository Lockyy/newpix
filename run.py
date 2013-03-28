import newpix
import sys
import logger

if __name__ == '__main__':
	sys.stdout = logger.logger()
	newpix = newpix.newpix()
	newpix.main()