# This subprogram calculate digit sum

import sys
import os

if __name__ == '__main__':
	# Get process arguments
	argv = sys.argv[1::]
	result = 0

	if len(argv) >= 2:
		for i in argv:
			result += int(i)

	print('Result: ' + str(result))