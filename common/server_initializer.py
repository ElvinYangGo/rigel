class ServerInitializer:
	def __init__(self):
		pass

	def init_server_handler_dispatcher(self):
		pass
	
	def init_global_data(self):
		pass
	
	def init_rmq(self):
		pass
	
	def send_init_request(self):
		pass
	
	def initialize(self):
		self.init_global_data()
		self.init_server_handler_dispatcher()
		self.init_rmq()
		self.send_init_request()
