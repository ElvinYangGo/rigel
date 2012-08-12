import zmq
from mq_client.rmq import RMQ
from common.global_data import GlobalData

class ServerInitializer(object):
	def __init__(self, pub_address, sub_address, server_name, pipeline):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_name = server_name
		self.pipeline = pipeline
		self.rmq = None
		
	def init_global_data(self):
		GlobalData.instance.zmq_context = zmq.Context()
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, GlobalData.instance.zmq_context, self.pipeline)
		self.rmq.subscribe(GlobalData.instance.server_name)
	
		GlobalData.instance.rmq = self.rmq
	
		self.rmq.start()
	
	def send_init_request(self):
		pass
	
	def initialize(self):
		self.init_global_data()
		self.init_rmq()
		self.send_init_request()
