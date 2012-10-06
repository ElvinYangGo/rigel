from common.heart_beat import HeartBeat
from common.global_data import GlobalData
from common.server_status import ServerStatus

class InitServerResHandler(object):
	def handle_message(self, message_id, channel_buffer, **kwargs):
		self.init_heart_beat()
		GlobalData.inst.server_status = ServerStatus.SERVER_STATUS_RUNNING
		print '%s init server res' % (GlobalData.inst.server_name)

	def init_heart_beat(self):
		GlobalData.inst.heart_beat = HeartBeat(GlobalData.inst.server_option_config.get_heart_beat_interval())
		GlobalData.inst.heart_beat.start()