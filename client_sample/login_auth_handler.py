from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2
from client_sample.client_global_data import ClientGlobalData
import client_sample.msg_sender

class LoginAuthHandler(object):
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
			#connect gateway
			ClientGlobalData.server_token = response.server_token
			ClientGlobalData.account_id = response.account_id
			ClientGlobalData.status = 2
			client_sample.msg_sender.connect(response.gateway_ip, response.gateway_port)
		elif response.result == ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_NOT_EXIST:
			client_sample.msg_sender.create_account()
		else:
			print 'login auth failed, error code: %x' % response.result
