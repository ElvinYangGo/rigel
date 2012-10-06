import threading
import time
from common.channel_name import ChannelName
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.server_status import ServerStatus
from common.global_data import GlobalData

class HeartBeatMonitor(threading.Thread):
	def __init__(self, heart_beat_interval, heart_beat_timeout, heart_beat_alive):
		self.heart_beat_interval = heart_beat_interval
		self.heart_beat_timeout = heart_beat_timeout
		self.heart_beat_alive = heart_beat_alive
		threading.Thread.__init__(self, name='heart_beat_monitor')
		
	def run(self):
		while True:
			self.change_server_status()
			self.broadcast_server_status()
			time.sleep(self.heart_beat_interval/1000)

	def change_server_status(self):
		current_time = time.time()
		for server in GlobalData.inst.server_manager.get_all_servers().itervalues():
			if server.running() and self.server_timeout(current_time, server):
				server.set_status(ServerStatus.SERVER_STATUS_CLOSED)
			if server.closed() and self.server_alive(current_time, server):
				server.set_status(ServerStatus.SERVER_STATUS_RUNNING)

	def broadcast_server_status(self):
		server_list_message = GlobalData.inst.server_manager.to_net()
		GlobalData.inst.rmq.send_message(
			server_list_message,
			ChannelName.SERVER_STATUS,
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)
		
	def server_timeout(self, current_time, server):
		return self.heart_beat_timeout / 1000 < current_time - server.get_heart_beat_time()

	def server_alive(self, current_time, server):
		return current_time - server.get_heart_beat_time() < self.heart_beat_alive / 1000
	
	def set_heart_beat_timeout(self, heart_beat_timeout):
		self.heart_beat_timeout = heart_beat_timeout

	def set_heart_beat_interval(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
