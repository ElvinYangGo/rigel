from network.channel import Channel

class ChannelPipeline:
	def __init__(self, handlers=None):
		if handlers:
			self.handlers = handlers
		else:
			self.handlers = []
		self.channel = None
		
	def append_handler(self, name, handler):
		self.handlers.append((name, handler))
	
	def remove_handler(self, name):
		self.handlers = [entry for entry in self.handlers if entry[0] != name]
	
	def set_channel(self, channel):
		self.channel = channel

	def handler_count(self):
		return len(self.handlers)

	def handle_connection(self):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handle_connection'):
				entry[1].handle_connection(self.channel)
			
	def handle_disconnection(self):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handle_disconnection'):
				entry[1].handle_disconnection(self.channel)

	def handle_upstream(self, channel_buffer, **kwargs):
		for entry in reversed(self.handlers):
			if hasattr(entry[1], 'handle_upstream'):
				channel_buffer = entry[1].handle_upstream(channel_buffer, channel=self.channel, **kwargs)
				if not channel_buffer:
					break

	def handle_downstream(self, channel_buffer, **kwargs):
		for entry in self.handlers:
			if hasattr(entry[1], 'handle_downstream'):
				channel_buffer = entry[1].handle_downstream(channel_buffer, channel=self.channel, **kwargs)
		return channel_buffer
		"""
		if isinstance(self.channel, Channel):
			self.channel.write_to_twisted_protocol(channel_buffer.read_all_data())
		else:
			pass"""