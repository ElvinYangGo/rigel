from network.channel_buffer import ChannelBuffer

class Channel:
	def __init__(self):
		self.channel_buffer = ChannelBuffer()
	
	def set_channel_pipeline(self, channel_pipeline):
		self.channel_pipeline = channel_pipeline
	
	def set_twisted_protocol(self, twisted_protocol):
		self.twisted_protocol = twisted_protocol

	def channel_buffer_readable_bytes(self):
		return self.channel_buffer.readable_bytes()

	def append_data(self, data):
		self.channel_buffer.append(data)
	
	def handle_connection(self):
		self.channel_pipeline.handle_connection()
	
	def handle_upstream(self):
		self.channel_pipeline.handle_upstream(self.channel_buffer)
	
	def send(self, channel_buffer, message_id=0):
		if message_id != 0:
			buffer_with_message_id = ChannelBuffer()
			buffer_with_message_id.write_int(message_id)
			buffer_with_message_id.append(channel_buffer.get_all_data())
			self.channel_pipeline.handle_downstream(buffer_with_message_id)
		else:
			self.channel_pipeline.handle_downstream(channel_buffer)

	def handle_disconnection(self):
		self.channel_pipeline.handle_disconnection()

	def write_to_twisted_protocol(self, data):
		self.twisted_protocol.transport.write(data)
		
	def get_remote_ip(self):
		return self.twisted_protocol.get_remote_ip()
	
	def get_remote_port(self):
		return self.twisted_protocol.get_remote_port()