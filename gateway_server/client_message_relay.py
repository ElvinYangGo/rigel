import protocol.server_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from protocol.client_protocol_id import ClientProtocolID
from gateway_server.gateway_global_data import GatewayGlobalData

class ClientMessageRelay:
	def handle_upstream(self, channel_buffer, **kwargs):
		channel = kwargs['channel']
		message_id = channel_buffer.get_int()
		protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper()
		protocol_wrapper.protocol_id = message_id
		protocol_wrapper.client_conn_info.client_id = channel.get_client_conn_info().get_client_id()
		protocol_wrapper.client_conn_info.gateway_server_name = channel.get_client_conn_info().get_gateway_server_name()
		protocol_wrapper.client_conn_info.game_server_name = channel.get_client_conn_info().get_game_server_name()
		protocol_wrapper.inner_protocol = channel_buffer.get_all_data()
		channel_name = self.get_channel_name(channel, message_id)
		GatewayGlobalData.inst.client_rmq_pub.send_message(
			protocol_wrapper,
			channel_name,
			ServerProtocolID.P_CLIENT_TO_SERVER_RELAY
			)

	def get_channel_name(self, channel, protocol_id):
		if (protocol_id & ClientProtocolID.ID_TYPE_MAGIC) == ClientProtocolID.ID_TYPE_CCENTER:
			return 'center_server'
		else:
			return channel.get_game_server_name()