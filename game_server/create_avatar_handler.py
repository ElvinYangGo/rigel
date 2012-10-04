from protocol.client_protocol_id import ClientProtocolID
from protocol.server_protocol_id import ServerProtocolID
import protocol.client_message_pb2
from plain_class.avatar import Avatar
from game_server.game_global_data import GameGlobalData

class CreateAvatarHandler(object):
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_CREATE_AVATAR_REQ,
			CreateAvatarHandler()
			)
		
	def handle_message(self, message_id, channel_buffer, **kwargs):
		client_conn_info = kwargs['client_conn_info']
		request = protocol.client_message_pb2.CreateAvatarReq.FromString(
			channel_buffer.read_all_data()
			)
		response = protocol.client_message_pb2.CreateAvatarRes()

		self.create_avatar(client_conn_info, request)

		response.result = ClientProtocolID.R_CREATE_AVATAR_RES_SUCCESS
		GameGlobalData.inst.rmq.send_message(
			response,
			client_conn_info.gateway_server_name,
			ServerProtocolID.P_SERVER_TO_CLIENT_RELAY,
			client_id=client_conn_info.client_id,
			inner_message_id=ClientProtocolID.P_CREATE_AVATAR_RES
			)

	def create_avatar(self, client_conn_info, request):
		account_id = client_conn_info.client_id
		r = GameGlobalData.inst.redis_cluster.get_redis(account_id)
		avatar = Avatar(account_id, request.name, request.gender, request.level)
		GameGlobalData.inst.plain_class_accessor.set_avatar(r, account_id, avatar)