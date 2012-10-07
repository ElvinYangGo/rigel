from common.server_status import ServerStatus

class Server(object):
	def __init__(self, name, type, status):
		self.name = name
		self.type = type
		self.status = status
		
	def get_name(self):
		return self.name
	
	def get_type(self):
		return self.type
	
	def get_status(self):
		return self.status

	def starting(self):
		return self.compare_status(ServerStatus.SERVER_STATUS_STARTING)

	def running(self):
		return self.compare_status(ServerStatus.SERVER_STATUS_RUNNING)

	def closed(self):
		return self.compare_status(ServerStatus.SERVER_STATUS_CLOSED)

	def compare_status(self, status):
		return True if self.status == status else False