from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2
import client_sample.msg_sender

class CreateAvatarHandler:
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_CREATE_AVATAR_RES,
			CreateAvatarHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		response = protocol.client_message_pb2.CreateAvatarRes.FromString(
			channel_buffer.read_all_data()
			)
		if response.result == ClientProtocolID.R_CREATE_AVATAR_RES_SUCCESS:
			print 'create avatar succeeded'
		else:
			print 'create avatar failed, error code: %x' % response.result
