from common.server_initializer import ServerInitializer
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from mq_client.rmq import RMQ
from common.channel_name import ChannelName
from master_server.heart_beat_monitor import HeartBeatMonitor

class MasterServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, handler_register, server_option_reader):
		ServerInitializer.__init__(self, pub_address, sub_address, server_name, handler_register)
		self.server_option_reader = server_option_reader
			
	def init_global_data(self):
		self.global_data = GlobalData()
		self.global_data.server_manager = ServerManager()
		self.global_data.server_option_reader = self.server_option_reader
		
		self.init_heart_beat_monitor()
		
		return self.global_data
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, self.server_handler_dispatcher)
		self.rmq.subscribe(ChannelName.SERVER_INITIALIZATION)
	
		self.global_data.rmq = self.rmq
		self.rmq.set_global_data(self.global_data)
	
		self.rmq.start()

		#move to another function
		self.rmq.subscribe(ChannelName.HEART_BEAT)

	def init_heart_beat_monitor(self):
		heart_beat_interval = self.server_option_reader.get_server_option_config().get_heart_beat_interval()
		heart_beat_timeout = self.server_option_reader.get_server_option_config().get_heart_beat_timeout()
		self.global_data.heart_beat_monitor = HeartBeatMonitor(self.global_data, heart_beat_interval, heart_beat_timeout)	
		self.global_data.heart_beat_monitor.start()
	