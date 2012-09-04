import uuid
import protocol.client_message_pb2
from auth_server.auth_global_data import AuthGlobalData
from protocol.client_protocol_id import ClientProtocolID
from plain_class.client_connection_info import ClientConnectionInfo

class LoginAuthHandler(object):
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_LOGIN_AUTH_REQ,
			LoginAuthHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		request = protocol.client_message_pb2.LoginAuthReq.FromString(
			channel_buffer.read_all_data()
			)
		response = protocol.client_message_pb2.LoginAuthRes()

		#check if name exist
		account_id = AuthGlobalData.inst.plain_class_accessor.get_user_name_to_id(
			AuthGlobalData.inst.redis_cluster.get_account_redis(),
			request.name
			)
		if account_id == 0:
			response.result = ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_NOT_EXIST
			channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_AUTH_RES)
			return

		#check if name and password valid
		user = AuthGlobalData.inst.plain_class_accessor.get_user(
			AuthGlobalData.inst.redis_cluster.get_account_redis(),
			account_id
			)
		if user.get_user_name() != request.name or user.get_password() != request.passord:
			response.result = ClientProtocolID.R_LOGIN_AUTH_USER_NAME_OR_PASSWORD_INVALID
			channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_AUTH_RES)
			return

		#all check passed
		#dispatch gateway server and game server
		#generate server token, send it to redis first, then client
		gateway_server = AuthGlobalData.inst.server_manager.dispatch_gateway_server()
		game_server = AuthGlobalData.inst.server_manager.dispatch_game_server()
		server_token = uuid.uuid1()
		token = ''.join([request.user_token, server_token])
		client_connection_info = ClientConnectionInfo(
			account_id,
			gateway_server.get_name(),
			game_server.get_name(),
			token
			)
		#send to redis by user id
		r = AuthGlobalData.insta.redis_cluster.get_redis(account_id)
		AuthGlobalData.inst.plain_class_accessor.set_client_connection_info(
			r,
			account_id,
			client_connection_info
			)
		AuthGlobalData.inst.plain_class_accessor.pexpire_client_connection_info(
			r,
			account_id,
			10000
			)
		#send to client
		response.result = ClientProtocolID.R_LOGIN_AUTH_USER_NAME_OR_PASSWORD_INVALID
		response.server_token = server_token
		#TODO gateway ip and port
		#response.gateway_ip =
		#response.gateway_port =
		response.account_id = account_id
		channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_AUTH_RES)