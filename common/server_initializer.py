from common.server_handler_dispatcher import ServerHandlerDispatcher
from mq_client.rmq import RMQ

class ServerInitializer:
	def __init__(self, pub_address, sub_address, server_name, handler_register):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_name = server_name
		self.handler_register = handler_register
		self.server_handler_dispatcher = None
		self.global_data = None
		self.rmq = None
		
	def init_server_handler_dispatcher(self):
		self.server_handler_dispatcher = self.handler_register.register(ServerHandlerDispatcher())
		return self.server_handler_dispatcher

	def init_global_data(self):
		pass
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, self.server_handler_dispatcher)
		self.rmq.subscribe(self.global_data.server_name)
	
		self.global_data.rmq = self.rmq
		self.rmq.set_global_data(self.global_data)
	
		self.rmq.start()
	
	def send_init_request(self):
		pass
	
	def initialize(self):
		self.init_global_data()
		self.init_server_handler_dispatcher()
		self.init_rmq()
		self.send_init_request()
