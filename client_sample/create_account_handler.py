from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2
import client_sample.msg_sender

class CreateAccountHandler:
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_CREATE_ACCOUNT_RES,
			CreateAccountHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		response = protocol.client_message_pb2.CreateAccountRes.FromString(
			channel_buffer.read_all_data()
			)
		if response.result == ClientProtocolID.R_CREATE_ACCOUNT_RES_SUCCESS:
			print 'create account succeeded'
			client_sample.msg_sender.send_login_auth_message()
		else:
			print 'create account failed, error code: %x' % response.result
