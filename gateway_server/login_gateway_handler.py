import protocol.client_message_pb2
from protocol.client_protocol_id import ClientProtocolID
from gateway_server.gateway_global_data import GatewayGlobalData
from common.util import send_result

class LoginGatewayHandler:
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
		client_connection_info = GatewayGlobalData.inst.plain_class_accessor.get_client_connection_info(
			r,
			request.account_id
			)

		#check if token matches
		valid, error = self.valid_token(request, client_connection_info)
		if not valid:
			send_result(
				channel,
				response,
				ClientProtocolID.P_LOGIN_GATEWAY_RES,
				error
				)
			return

		#login ok, add channel to channel manager, send result to client
		channel_manager = channel.get_channel_manager()
		channel_manager.insert(request.account_id, channel)
		channel.set_client_connection_info(client_connection_info)

		send_result(
			channel,
			response,
			ClientProtocolID.P_LOGIN_GATEWAY_RES,
			ClientProtocolID.R_LOGIN_GATEWAY_RES_SUCCESS
			)

	def valid_token(self, request, client_connection_info):
		if client_connection_info is None:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED

		if client_connection_info.get_token() != request.token:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_INVALID

		return True, None