import protocol.server_message_pb2
import protocol.client_message_pb2
from protocol.client_protocol_id import ClientProtocolID
from protocol.server_protocol_id import ServerProtocolID
from gateway_server.gateway_global_data import GatewayGlobalData
from common.util import send_result

class LoginGatewayHandler(object):
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_LOGIN_GATEWAY_REQ,
			LoginGatewayHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		request = protocol.client_message_pb2.LoginGatewayReq.FromString(
			channel_buffer.read_all_data()
			)
		response = protocol.client_message_pb2.LoginGatewayRes()

		#get client connection info from redis
		r = GatewayGlobalData.inst.redis_cluster.get_redis(request.account_id)
		client_conn_info = GatewayGlobalData.inst.plain_class_accessor.get_client_conn_info(
			r,
			request.account_id
			)

		#check if token matches
		valid, error = self.valid_token(request, client_conn_info)
		if not valid:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_GATEWAY_RES,
				error
				)
			return

		#check if game server running
		if not GatewayGlobalData.inst.server_manager.server_running(client_conn_info.get_game_server_name()):
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_GATEWAY_RES,
				ClientProtocolID.R_LOGIN_GATEWAY_RES_GAME_SERVER_CLOSED
				)
			return

		#login ok, add channel to channel manager, send result to client
		channel_manager = channel.get_channel_manager()
		channel_manager.insert(request.account_id, channel)
		channel.set_client_conn_info(client_conn_info)

		send_result(
			channel,
			response,
			ClientProtocolID.P_LOGIN_GATEWAY_RES,
			ClientProtocolID.R_LOGIN_GATEWAY_RES_SUCCESS
			)

		#send prepare avatar notice to game server
		self.send_prepare_avatar_notice(request.account_id, client_conn_info.get_game_server_name())

	def valid_token(self, request, client_connection_info):
		if client_connection_info is None:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED

		if client_connection_info.get_token() != request.token:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_INVALID

		return True, None

	def send_prepare_avatar_notice(self, account_id, game_server_name):
		prepare_avatar_notice = protocol.server_message_pb2.PrepareAvatarNotice()
		prepare_avatar_notice.account_id = account_id
		GatewayGlobalData.inst.client_rmq_pub.send_message(
			prepare_avatar_notice,
			game_server_name,
			ServerProtocolID.P_PREPARE_AVATAR_NOTICE
			)