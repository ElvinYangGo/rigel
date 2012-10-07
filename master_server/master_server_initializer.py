from master_server.master_global_data import MasterGlobalData
from common.server_initializer import ServerInitializer
from master_server.master_server_manager import MasterServerManager
from mq_client.rmq import RMQ
from mq_client.rmq_pub import RMQPub
from common.channel_name import ChannelName
from master_server.heart_beat_monitor import HeartBeatMonitor
from common.global_data import GlobalData
from common.server_status import ServerStatus

class MasterServerInitializer(ServerInitializer):
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
		super(MasterServerInitializer, self).__init__(
			pub_address,
			sub_address,
			server_name,
			pipeline,
			redis_server_file_name,
			redis_partition_file_name,
			server_option_file_name
			)
			
	def init_global_data(self):
		GlobalData.inst = MasterGlobalData()
		super(MasterServerInitializer, self).init_global_data()
		GlobalData.inst.server_manager = MasterServerManager()
		GlobalData.inst.server_status = ServerStatus.SERVER_STATUS_RUNNING
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, GlobalData.inst.zmq_context, self.pipeline)
		GlobalData.inst.rmq = self.rmq
		self.rmq.start()
		self.rmq.subscribe(ChannelName.SERVER_INIT)

		#move to another function ?
		self.rmq.subscribe(ChannelName.HEART_BEAT)

		GlobalData.inst.heart_beat_rmq_pub = RMQPub(self.pub_address, GlobalData.inst.zmq_context, self.pipeline)
		self.init_heart_beat_monitor()

	def init_heart_beat_monitor(self):
		heart_beat_interval = GlobalData.inst.server_option_config.get_heart_beat_interval()
		heart_beat_timeout = GlobalData.inst.server_option_config.get_heart_beat_timeout()
		heart_beat_alive = GlobalData.inst.server_option_config.get_heart_beat_alive()
		GlobalData.inst.heart_beat_monitor = HeartBeatMonitor(
			heart_beat_interval,
			heart_beat_timeout,
			heart_beat_alive
			)
		GlobalData.inst.heart_beat_monitor.start()
	