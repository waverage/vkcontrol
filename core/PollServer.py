import requests
import json
from config.Config import Config

class PollServer:
	def __init__(self, apiObject):
		self.api = apiObject
		self.during = 50

	def prepareUrl(self, data):
		return 'https://' + str(data['server']) + '?act=a_check&key=' + str(data['key']) + '&ts=' + str(data['ts']) + '&wait=' + str(self.during) + '&mode=2&version=1'
		
	def getUpdates(self):
		server = self.api.messages.getLongPollServer(need_pts=1)
		response = requests.get(self.prepareUrl(server));
		return json.loads(response.text)

	def getLastMessageEvent(self):
		data = self.getUpdates()
		events = data['updates']

		return self.getMessageFromUpdates(events)

	def getMessageFromUpdates(self, events):
		for event in events:
			if event[0] == 4 and len(event) > 3:
				if str(event[3]) == Config.USER_ID:
					return event
		return 'None'

	def sendResponse(self, response):
		self.api.messages.send(user_id=Config.USER_ID, message=response)