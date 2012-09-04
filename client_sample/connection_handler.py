from client_sample.client_global_data import ClientGlobalData
import protocol.client_message_pb2
from protocol.client_protocol_id import ClientProtocolID

class ConnectionHandler(object):
	def handle_connection(self, channel):
		print 'channel connected'
		ClientGlobalData.channel = channel

		#send login request
		self.send_login_auth_message()
		#self.send_login_gateway_message()

	def handle_disconnection(self, channel):
		print 'channel disconnected'

	def send_login_auth_message(self):
		request = protocol.client_message_pb2.LoginAuthReq()
		request.name = 'aaa'
		request.password = 'ppp'
		request.user_token = 'ttt'
		ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_LOGIN_AUTH_REQ)

	def send_login_gateway_message(self):
		request = protocol.client_message_pb2.LoginGatewayReq()
		request.account_id = 111
		request.token = 'ttt'
		ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_LOGIN_GATEWAY_REQ)
