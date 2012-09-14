import uuid
import protocol.client_message_pb2
from auth_server.auth_global_data import AuthGlobalData
from protocol.client_protocol_id import ClientProtocolID
from plain_class.client_connection_info import ClientConnectionInfo
from common.util import send_result
from common.server_type import ServerType

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
		ok, account_id = self.valid_user_name(request)
		if not ok:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_AUTH_RES,
				ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_NOT_EXIST
				)
			return

		#check if name and password valid
		ok = self.valid_user_name_and_password(request, account_id)
		if not ok:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_AUTH_RES,
				ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_OR_PASSWORD_INVALID
				)
			return

		#all check passed
		#dispatch gateway server and game server
		#generate server token, send it to redis first, then client
		gateway_server = AuthGlobalData.inst.server_manager.dispatch_server(ServerType.GATEWAY_SERVER)
		if gateway_server is None:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_AUTH_RES,
				ClientProtocolID.R_LOGIN_AUTH_RES_NO_GATEWAY_SERVER
				)
			return
		
		game_server = AuthGlobalData.inst.server_manager.dispatch_server(ServerType.GAME_SERVER)
		if game_server is None:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_AUTH_RES,
				ClientProtocolID.R_LOGIN_AUTH_RES_NO_GAME_SERVER
				)
			return
		
		server_token = uuid.uuid1()
		token = ''.join([request.user_token, str(server_token)])
		self.save_client_connection_info_to_redis(account_id, token, gateway_server, game_server)

		#send to client
		response = self.fill_success_response(response, account_id, server_token, gateway_server)
		send_result(
			channel,
			response,
			ClientProtocolID.P_LOGIN_AUTH_RES,
			ClientProtocolID.R_LOGIN_AUTH_RES_SUCCESS
			)
		
	def valid_user_name(self, request):
		account_id = AuthGlobalData.inst.plain_class_accessor.get_user_name_to_id(
			AuthGlobalData.inst.redis_cluster.get_account_redis(),
			request.name
			)
		if account_id == 0:
			return False, account_id
		else:
			return True, account_id
		
	def valid_user_name_and_password(self, request, account_id):
		user = AuthGlobalData.inst.plain_class_accessor.get_user(
			AuthGlobalData.inst.redis_cluster.get_account_redis(),
			account_id
			)
		if user.get_user_name() != request.name or user.get_password() != request.password:
			return False
		else:
			return True

	def save_client_connection_info_to_redis(self, account_id, token, gateway_server, game_server):
		client_connection_info = ClientConnectionInfo(
			account_id,
			gateway_server.get_name(),
			game_server.get_name(),
			token
			)
		#send to redis by user id
		r = AuthGlobalData.inst.redis_cluster.get_redis(account_id)
		AuthGlobalData.inst.plain_class_accessor.set_client_connection_info(
			r,
			account_id,
			client_connection_info
			)
		AuthGlobalData.inst.plain_class_accessor.expire_client_connection_info(
			r,
			account_id,
			100
			)
		
	def fill_success_response(self, response, account_id, server_token, gateway_server):
		response.server_token = str(server_token)
		response.gateway_ip = AuthGlobalData.inst.gateway_address.get_wan_ip(gateway_server.get_name())
		response.gateway_port = AuthGlobalData.inst.gateway_address.get_port(gateway_server.get_name())
		response.account_id = account_id
		return response
	