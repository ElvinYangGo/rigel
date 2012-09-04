from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2

class LoginAuthHandler:
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_LOGIN_AUTH_RES,
			LoginAuthHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		response = protocol.client_message_pb2.LoginAuthRes.FromString(
			channel_buffer.read_all_data()
			)
		if response.result == ClientProtocolID.R_LOGIN_AUTH_RES_SUCCESS:
			print 'login auth succeeded'
		else:
			print 'login auth failed, error code: %x' % response.result

