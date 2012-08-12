import protocol.protocol_data_pb2

class ServerMessageRelay(object):
	def handle_upstream(self, channel_buffer, **kwargs):
		protocol_wrapper = protocol.protocol_data_pb2.ProtocolWrapper.FromString(channel_buffer.get_all_data())
		channel = GlobalData.instance.channel_mananger.get_channel(protocol_wrapper.client_id)
		if not channel:
			channel.send(protocol_wrapper.inner_protocol, protocol_wrapper.protocol_id)