import protocol
from protocol.server_protocol_id import ServerProtocolID
from gateway_server.gateway_global_data import GatewayGlobalData

class ClientMessageRelay:
	def handle_upstream(self, channel_buffer, **kwargs):
		channel = kwargs['channel']
		message_id = channel_buffer.get_int()
		protocol_wrapper = protocol.server_data_pb2.ProtocolWrapper()
		protocol_wrapper.protocol_id = message_id
		protocol_wrapper.client_id = channel.get_client_id()
		protocol_wrapper.inner_protocol = channel_buffer.get_all_data()
		#TODO: send to different server in terms of message_id
		GatewayGlobalData.rmq_pub.send_message_string(
			protocol_wrapper,
			channel.get_game_server_name(),
			ServerProtocolID.P_CLIENT_TO_GAME_SERVER_RELAY
			)
