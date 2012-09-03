import zmq
from mq_client.rmq import RMQ
from common.global_data import GlobalData
from cluster.redis_cluster import RedisCluster

class ServerInitializer(object):
	def __init__(
		self,
		pub_address,
		sub_address,
		server_name,
		pipeline,
		redis_server_file_name,
		redis_partition_file_name
		):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_name = server_name
		self.pipeline = pipeline
		self.rmq = None
		self.redis_server_file_name = redis_server_file_name
		self.redis_partition_file_name = redis_partition_file_name
		
	def init_global_data(self):
		GlobalData.inst.zmq_context = zmq.Context()
		GlobalData.inst.redis_cluster = RedisCluster(
			self.redis_server_file_name,
			self.redis_partition_file_name
			)
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, GlobalData.inst.zmq_context, self.pipeline)
		self.rmq.subscribe(GlobalData.inst.server_name)
	
		GlobalData.inst.rmq = self.rmq
	
		self.rmq.start()
	
	def send_init_request(self):
		pass
	
	def initialize(self):
		self.init_global_data()
		self.init_rmq()
		self.send_init_request()
