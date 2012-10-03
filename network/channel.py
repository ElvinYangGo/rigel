from twisted.internet import reactor
from network.channel_buffer import ChannelBuffer

class Channel:
	def __init__(self):
		self.channel_buffer = ChannelBuffer()
		self.client_conn_info = None
		self.channel_manager = None
	
	def set_channel_pipeline(self, channel_pipeline):
		self.channel_pipeline = channel_pipeline
	
	def set_twisted_protocol(self, twisted_protocol):
		self.twisted_protocol = twisted_protocol

	def channel_buffer_readable_bytes(self):
		return self.channel_buffer.readable_bytes()

	def append_data(self, data):
		self.channel_buffer.append(data)
		self.handle_upstream()
	
	def handle_connection(self):
		self.channel_pipeline.handle_connection()
	
	def handle_upstream(self):
		self.channel_pipeline.handle_upstream(self.channel_buffer)

	def send_string(self, message_string, message_id=0):
		channel_buffer = ChannelBuffer(message_string)
		self.send_channel_buffer(channel_buffer, message_id)
	
	def send_channel_buffer(self, channel_buffer, message_id=0):
		if message_id != 0:
			buffer_with_message_id = ChannelBuffer()
			buffer_with_message_id.write_int(message_id)
			buffer_with_message_id.append(channel_buffer.get_all_data())
			self.send(buffer_with_message_id)
			#self.channel_pipeline.handle_downstream(buffer_with_message_id)
		else:
			#self.channel_pipeline.handle_downstream(channel_buffer)
			self.send(channel_buffer)

	def send(self, channel_buffer):
		buffer_to_send = self.channel_pipeline.handle_downstream(channel_buffer)
		self.write_to_twisted_protocol(buffer_to_send.read_all_data())

	def handle_disconnection(self):
		self.channel_pipeline.handle_disconnection()
		if self.channel_manager and self.client_conn_info:
			self.channel_manager.remove(self.client_conn_info.get_client_id())
		self.channel_pipeline = None
		self.channel_buffer = None
		self.client_conn_info = None
		self.twisted_protocol = None

	def write_to_twisted_protocol(self, data):
		reactor.callFromThread(Channel.write_to_twisted_protocol_not_safe, self, data)

	def write_to_twisted_protocol_not_safe(channel, data):
		channel.twisted_protocol.transport.write(data)
		
	def get_remote_ip(self):
		return self.twisted_protocol.get_remote_ip()
	
	def get_remote_port(self):
		return self.twisted_protocol.get_remote_port()

	def set_client_conn_info(self, client_conn_info):
		self.client_conn_info = client_conn_info
		
	def get_client_conn_info(self):
		return self.client_conn_info

	def get_client_id(self):
		return self.client_conn_info.get_client_id()

	def get_game_server_name(self):
		return self.client_conn_info.get_game_server_name()
	
	def get_channel_manager(self):
		return self.channel_manager

	def set_channel_manager(self, channel_manager):
		self.channel_manager = channel_manager