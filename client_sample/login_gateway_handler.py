from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2
import client_sample.msg_sender

class LoginGatewayHandler:
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_LOGIN_GATEWAY_RES,
			LoginGatewayHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		response = protocol.client_message_pb2.LoginGatewayRes.FromString(
			channel_buffer.read_all_data()
			)
		if response.result == ClientProtocolID.R_LOGIN_GATEWAY_RES_SUCCESS:
			print 'login gateway succeeded'
			client_sample.msg_sender.create_avatar()
		else:
			print 'login gateway failed, error code: %x' % response.result

