from common.server_initializer import ServerInitializer
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID
from game_server.global_data import GlobalData
from common.server_manager import ServerManager
import protocol.protocol_message_pb2
from common.server_type import ServerType
from mq_client.rmq import RMQ
from game_server.handler_register import HandlerRegister

class GameServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_name = server_name
		self.server_handler_dispatcher = None
		self.global_data = None
		self.rmq = None
		
	def init_server_handler_dispatcher(self):
		handler_register = HandlerRegister()
		self.server_handler_dispatcher = handler_register.register(ServerHandlerDispatcher())
		return self.server_handler_dispatcher
		def init_global_data(self):
		self.global_data = GlobalData()
		self.global_data.server_manager = ServerManager()
		self.global_data.server_name = self.server_name
		return self.global_data
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, self.server_handler_dispatcher)
		self.rmq.subscribe(self.global_data.server_name)
	
		self.global_data.rmq = self.rmq
		self.rmq.set_global_data(self.global_data)
	
		self.rmq.start()

	def send_init_request(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = self.global_data.server_name		
		message.type = ServerType.GAME_SERVER
		self.rmq.send_message_string(message, u'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

