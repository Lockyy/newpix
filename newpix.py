import newpixchecker
import sys
import logger

if __name__ == '__main__':
	sys.stdout = logger.logger()
	newpixchecker = newpixchecker.newpixchecker()
	newpixchecker.main()
