from common.server_status import ServerStatus
import protocol.protocol_pb2

class Server:
	def __init__(self, name):
		self.status = ServerStatus.SERVER_STATUS_STARTING
		self.name = name
		
	def get_name(self):
		return self.name
	
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
		message = protocol.protocol_pb2.Server()
		message.name = self.name
		message.status = self.status
		return message
	
	def to_net_string(self):
		return self.to_net().SerializeToString()