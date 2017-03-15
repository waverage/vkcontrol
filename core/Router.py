import re
import os
from subprocess import *

class Router:
	def __init__(self):
		self.COMMANDS_DIR = 'commands'
		self.COMMAND_PATTERN = re.compile('^(\S+)(:[\s|](.+)$|$)')

	def prepareCommand(self, route):
		match = re.match(self.COMMAND_PATTERN, route)
		if match == None:
			return False

		command = match.groups()[0]
		argv = match.groups()[2]

		files = os.listdir(self.COMMANDS_DIR)

		if command + '.py' in files:
			commandFile = self.COMMANDS_DIR + '/' + command + '.py'
			return (commandFile, argv)
		else:
			False

	def process(self, route):
		prepareResponse = self.prepareCommand(route)

		if prepareResponse[0] == False:
			return False

		commandFile, arguments = prepareResponse

		if arguments == None:
			arguments = ''

		if commandFile != False:
			# Open subprocess for run command in command line
			process = Popen('python ' + commandFile + ' ' + arguments, shell=True, stdout=PIPE, stdin=PIPE)
			# Read subprocess response
			return process.stdout.read()
		else:
			return False