from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from network.channel_buffer import ChannelBuffer

class ProtocolWrapperHandler(object):
	def __init__(self, handler_dispatcher):
		self.handler_dispatcher = handler_dispatcher
	
	def handle_upstream(self, channel_buffer, **kwargs):
		message_id = channel_buffer.get_int()
		if message_id == ServerProtocolID.P_CLIENT_TO_SERVER_RELAY:
			channel_buffer.skip_data(4)
			protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper.FromString(channel_buffer.get_all_data())
			channel_buffer = ChannelBuffer(protocol_wrapper.inner_protocol)
			self.handler_dispatcher.handle_upstream(
				channel_buffer, 
				client_conn_info=protocol_wrapper.client_conn_info,
				**kwargs
				)
		else:
			return channel_buffer

	def handle_downstream(self, channel_buffer, **kwargs):
		if not kwargs.has_key('inner_message_id') or not kwargs.has_key('client_id'):
			return channel_buffer
		if 0x5000 <= kwargs['inner_message_id']:
			return channel_buffer
		protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper()
		protocol_wrapper.protocol_id = kwargs['inner_message_id']
		protocol_wrapper.client_conn_info.client_id = kwargs['client_id']
		protocol_wrapper.inner_protocol = channel_buffer.read_all_data()
		return ChannelBuffer(protocol_wrapper.SerializeToString())