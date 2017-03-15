import re
import vk
import requests
import os
import json
import time
import random
from datetime import datetime
from config.Config import Config
from core.Router import Router
from core.PollServer import PollServer
import html

def initSession(config):
	session = vk.AuthSession(app_id=config.APP_ID, user_login=config.LOGIN, user_password=config.PASSWORD, scope='messages')
	return vk.API(session)

if __name__ == '__main__':
	# Create vk session using vk sdk
	vkapi = initSession(Config)
	# router need for process input command
	router = Router()
	# pollServer need to received events from vk site
	pollServer = PollServer(vkapi)

	print('Server is run')
	pollServer.sendResponse('Connected to server')
	while True:
		messageEvent = pollServer.getLastMessageEvent()
		if messageEvent != 'None':
			# Get event content
			message = messageEvent[6]
			message = html.unescape(message)
			try:
				result = router.process(message)
				pollServer.sendResponse(result)
			except BaseException:
				print('Process error')
				pass