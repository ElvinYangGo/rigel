from common.server_initializer import ServerInitializer
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID
from master_server.start_server_init_request_handler import StartServerInitRequestHandler
from master_server.end_server_init_notification_handler import EndServerInitNotificationHandler
from master_server.global_data import GlobalData
from master_server.server_manager import ServerManager
from mq_client.rmq import RMQ
from master_server.handler_register import HandlerRegister

class MasterServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_handler_dispatcher = None
		self.global_data = None
		self.rmq = None
				
	def init_server_handler_dispatcher(self):
		handler_register = HandlerRegister(ServerHandlerDispatcher())
		self.server_handler_dispatcher = handler_register.register()
		return self.server_handler_dispatcher
	def init_global_data(self):
		self.global_data = GlobalData()
		self.global_data.server_manager = ServerManager()
		return self.global_data
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, self.server_handler_dispatcher)
		self.rmq.subscribe(u'server_initialization')
	
		self.global_data.rmq = self.rmq
		self.rmq.set_global_data(self.global_data)
	
		self.rmq.start()

