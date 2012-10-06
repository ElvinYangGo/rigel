import zmq
from mq_client.rmq import RMQ
from mq_client.rmq_pub import RMQPub
from common.global_data import GlobalData
from cluster.redis_cluster import RedisCluster
from plain_class.plain_class_accessor import PlainClassAccessor
from common.server_status import ServerStatus
from common.server_option_config import ServerOptionConfig
from common.channel_name import ChannelName

class ServerInitializer(object):
	def __init__(
		self,
		pub_address,
		sub_address,
		server_name,
		pipeline,
		redis_server_file_name,
		redis_partition_file_name,
		server_option_file_name
		):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_name = server_name
		self.pipeline = pipeline
		self.rmq = None
		self.redis_server_file_name = redis_server_file_name
		self.redis_partition_file_name = redis_partition_file_name
		self.server_option_file_name = server_option_file_name
		
	def init_global_data(self):
		GlobalData.inst.zmq_context = zmq.Context()
		GlobalData.inst.redis_cluster = RedisCluster(
			self.redis_server_file_name,
			self.redis_partition_file_name
			)
		GlobalData.inst.plain_class_accessor = PlainClassAccessor()
		GlobalData.inst.server_option_config = ServerOptionConfig(config_file_name=self.server_option_file_name)
		GlobalData.inst.server_name = self.server_name
		GlobalData.inst.server_status = ServerStatus.SERVER_STATUS_STARTING
	
	def init_rmq(self):	
		GlobalData.inst.heart_beat_rmq_pub = RMQPub(self.pub_address, GlobalData.inst.zmq_context, self.pipeline)

		self.rmq = RMQ(self.pub_address, self.sub_address, GlobalData.inst.zmq_context, self.pipeline)
		GlobalData.inst.rmq = self.rmq
		self.rmq.start()
		self.rmq.subscribe(GlobalData.inst.server_name)
		self.rmq.subscribe(ChannelName.SERVER_STATUS)
	
	def send_init_request(self):
		pass
	
	def initialize(self):
		self.init_global_data()
		self.init_rmq()
		self.send_init_request()
