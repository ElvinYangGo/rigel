import protocol.server_message_pb2
from gateway_server.gateway_global_data import GatewayGlobalData

class ServerMessageRelay(object):
	def handle_upstream(self, channel_buffer, **kwargs):
		protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper.FromString(channel_buffer.get_all_data())
		channel = GatewayGlobalData.inst.channel_manager.get_channel(protocol_wrapper.client_conn_info.client_id)
		if channel is not None:
			channel.send_string(protocol_wrapper.inner_protocol, protocol_wrapper.protocol_id)