import time
from common.server_status import ServerStatus
from common.server import Server
import protocol.server_data_pb2

class ServerInMaster(Server):
	def __init__(self, name, type):
		super(ServerInMaster, self).__init__(name, type, ServerStatus.SERVER_STATUS_RUNNING)
		self.clear()

	def clear(self):
		self.status = ServerStatus.SERVER_STATUS_RUNNING
		self.heart_beat_time = time.time()
		
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
