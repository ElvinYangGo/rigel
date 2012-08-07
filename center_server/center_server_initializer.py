from common.server_initializer import ServerInitializer
from protocol.protocol_id import ProtocolID
from common.server_manager import ServerManager
import protocol.protocol_message_pb2
from common.server_type import ServerType

class CenterServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, handler_register, global_data):
		super(ServerInitializer, self).__init__(pub_address, sub_address, server_name, handler_register, global_data)

	def init_global_data(self):
		self.global_data.server_manager = ServerManager()
		self.global_data.server_name = self.server_name
		return self.global_data
	
	def send_init_request(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = self.global_data.server_name		
		message.type = ServerType.CENTER_SERVER
		self.rmq.send_message_string(message, u'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

