import protocol
from protocol.client_protocol_id import ClientProtocolID

class LoginGatewayHandler:
	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		request = protocol.client_message_pb2.LoginGatewayReq.FromString(
			channel_buffer.read_all_data()
			)
		response = protocol.client_message_pb2.LoginGatewayRes()

		#get client connection info from redis
		#check if token matches
		r = AuthGlobalData.insta.redis_cluster.get_redis(request.account_id)
		client_connection_info = GatewayGlobalData.inst.plain_class_accessor.get_client_connection_info(
			r,
			request.account_id
			)
		if client_connection_info is None:
			response.result = ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED
			channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_GATEWAY_RES)
			return

		if client_connection_info.get_token() != request.token:
			response.result = ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_INVALID
			channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_GATEWAY_RES)
			return

		#login ok, add channel to channel manager, send result to client
		channel_manager = channel.get_channel_manager()
		channel_manager.insert(request.account_id, channel)

		response.result = ClientProtocolID.R_LOGIN_GATEWAY_RES_SUCCESS
		channel.send_string(response.SerializeToString(), ClientProtocolID.P_LOGIN_GATEWAY_RES)
