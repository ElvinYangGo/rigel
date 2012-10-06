import json
from common.heart_beat import HeartBeat
from common.global_data import GlobalData
from common.channel_name import ChannelName
import protocol.server_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from common.server_option_config import ServerOptionConfig

class StartServerInitResHandler(object):
	def init_heart_beat(self, server_option_config):
		heart_beat_interval = server_option_config.get_heart_beat_interval()
		if not hasattr(GlobalData.inst, u'heart_beat'):
			GlobalData.inst.heart_beat = HeartBeat(heart_beat_interval)
			GlobalData.inst.heart_beat.start()
		else:
			GlobalData.inst.heart_beat.set_heart_beat_interval(heart_beat_interval)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.StartServerInitRes.FromString(
			channel_buffer.read_all_data()
			)
		if message.HasField('config'):
			config = json.loads(message.config)
			if config.has_key(u'server_option_config'):
				server_option_config = ServerOptionConfig(config_string=config['server_option_config'])
				self.init_heart_beat(server_option_config)

		GlobalData.inst.rmq.subscribe(ChannelName.SERVER_STATUS)
		message_to_send = protocol.server_message_pb2.EndServerInitNotice()
		message_to_send.name = GlobalData.inst.server_name
		GlobalData.inst.rmq.send_message(
			message_to_send, ChannelName.SERVER_INIT, ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
		print '%s send end_server_init_notice' % (GlobalData.inst.server_name)