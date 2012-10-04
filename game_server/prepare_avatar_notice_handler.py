from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.global_data import GlobalData

class PrepareAvatarNoticeHandler(object):
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_PREPARE_AVATAR_NOTICE,
			PrepareAvatarNoticeHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.StartServerInitRes.FromString(
			channel_buffer.read_all_data()
			)
