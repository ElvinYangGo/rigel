from common.server_initializer import ServerInitializer
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from mq_client.rmq import RMQ

class MasterServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, handler_register):
		ServerInitializer.__init__(self, pub_address, sub_address, server_name, handler_register)
			
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

