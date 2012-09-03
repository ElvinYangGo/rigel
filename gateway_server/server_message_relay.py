import protocol

class ServerMessageRelay(object):
	def handle_upstream(self, channel_buffer, **kwargs):
		protocol_wrapper = protocol.server_data_pb2.ProtocolWrapper.FromString(channel_buffer.get_all_data())
		channel = GlobalData.inst.channel_mananger.get_channel(protocol_wrapper.client_id)
		if channel is not None:
			channel.send_string(protocol_wrapper.inner_protocol, protocol_wrapper.protocol_id)