import protocol.protocol_data_pb2
from protocol.protocol_id import ProtocolID
from network.channel_buffer import ChannelBuffer

class ClientMessageRelay:
	def handle_upstream(self, channel_buffer, **kwargs):
		message_id = channel_buffer.get_int()
		protocol_wrapper = protocol.protocol_data_pb2.ProtocolWrapper()
		protocol_wrapper.protocol_id = message_id
		protocol_wrapper.inner_protocol = channel_buffer.get_all_data()
		protocol_wrapper.client_id = channel.get_client_id()
		#TODO: send to different server in terms of message_id
		channel = kwargs['channel']
		GatewayGlobalData.rmq_pub.send_message_string(
			message,
			channel.get_game_server_name(),
			ProtocolID.CLIENT_TO_GAME_SERVER_RELAY
			)

	"""
	def handle_downstream(self, channel_buffer, **kwargs):
		#TODO: if it is a gateway server's message, do not need to unpack it
		protocol_wrapper = protocol.protocol_data_pb2.ProtocolWrapper.FromString(channel_buffer.get_all_data())
		buffer_to_send = ChannelBuffer()
		buffer_to_send.write_int(protocol_wrapper.protocol_id)
		buffer_to_send.append(protocol_wrapper.inner_protocol)
		return buffer_to_send
	"""