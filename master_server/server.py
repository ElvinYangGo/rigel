from common.server_status import ServerStatus
import protocol.server_data_pb2

class Server:
	def __init__(self, name, type):
		self.status = ServerStatus.SERVER_STATUS_STARTING
		self.name = name
		self.type = type
		self.heart_beat_time = 0
		
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

	def set_status(self, status):
		self.status = status
		
	def to_net(self):
		message = protocol.server_data_pb2.Server()
		message.name = self.name
		message.status = self.status
		message.type = self.type
		return message
	
	def to_net_string(self):
		return self.to_net().SerializeToString()
	
	def get_heart_beat_time(self):
		return self.heart_beat_time
	
	def set_heart_beat_time(self, heart_beat_time):
		self.heart_beat_time = heart_beat_time
