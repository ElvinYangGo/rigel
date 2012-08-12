import threading
import time
from common.channel_name import ChannelName
from protocol.protocol_id import ProtocolID
import protocol
from common.server_status import ServerStatus
from common.global_data import GlobalData

class HeartBeatMonitor(threading.Thread):
	def __init__(self, heart_beat_interval, heart_beat_timeout):
		self.heart_beat_interval = heart_beat_interval
		self.heart_beat_timeout = heart_beat_timeout
		threading.Thread.__init__(self, name='heart_beat_monitor')
		
	def run(self):
		while True:
			closed_server_list = []
			current_time = time.time()
			for server in GlobalData.instance.server_manager.get_all_servers().itervalues():
				if server.running() and self.server_timeout(current_time, server):
					server.set_status(ServerStatus.SERVER_STATUS_CLOSED)
					closed_server_list.append(server)
			
			if closed_server_list:
				server_message = protocol.protocol_message_pb2.SynchronizeServerNotification()
				for closed_server in closed_server_list:
					server_message.servers.extend([closed_server.to_net()])
				GlobalData.instance.rmq.send_message_string(server_message, ChannelName.SERVER_STATUS, ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)
		
			time.sleep(self.heart_beat_interval/1000)
			
	def server_timeout(self, current_time, server):
		return self.heart_beat_timeout / 1000 < current_time - server.get_heart_beat_time()
	
	def set_heart_beat_timeout(self, heart_beat_timeout):
		self.heart_beat_timeout = heart_beat_timeout

	def set_heart_beat_interval(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
