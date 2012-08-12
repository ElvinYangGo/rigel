import threading
import time
from common.channel_name import ChannelName
from protocol.protocol_id import ProtocolID
import protocol
from common.global_data import GlobalData

class HeartBeat(threading.Thread):
	def __init__(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
		threading.Thread.__init__(self, name='heart_beat')
		
	def run(self):
		while True:
			message = protocol.protocol_message_pb2.HeartBeatNotification()
			message.name = GlobalData.instance.server_name
			GlobalData.instance.rmq.send_message_string(message, ChannelName.HEART_BEAT, ProtocolID.HEART_BEAT_NOTIFICATION)
			time.sleep(self.heart_beat_interval/1000)
			
	def set_heart_beat_interval(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
