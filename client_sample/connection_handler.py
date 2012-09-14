from client_sample.client_global_data import ClientGlobalData
import client_sample.msg_sender

class ConnectionHandler(object):
	def handle_connection(self, channel):
		print 'channel connected'
		ClientGlobalData.channel = channel

		#send login request
		#client_sample.msg_sender.create_account()
		if ClientGlobalData.status == 1:
			client_sample.msg_sender.send_login_auth_message()
		elif ClientGlobalData.status == 2:
			token = ''.join(['ttt', ClientGlobalData.server_token])
			client_sample.msg_sender.send_login_gateway_message(ClientGlobalData.account_id, token)

	def handle_disconnection(self, channel):
		print 'channel disconnected'

