class HandlerDispatcher:
	def __init__(self):
		self.handlers = {}
		
	def append_handler(self, key, handler):
		self.handlers[key] = handler
		
	def handle_connection(self, channel):
		for handler in self.handlers.values():
			if hasattr(handler, 'handle_connection'):
				handler.handle_connection(channel)
				break;

	def handle_disconnection(self, channel):
		for handler in self.handlers.values():
			if hasattr(handler, 'handle_disconnection'):
				handler.handle_disconnection(channel)
				break;

	def handle_upstream(self, channel_buffer, **kwargs):
		message_id = channel_buffer.get_int()
		if self.handlers.has_key(message_id):
			channel_buffer.skip_data(4)
			handler = self.handlers.get(message_id)
			handler.handle_message(message_id, channel_buffer, **kwargs)
		else:
			#send to upstream
			return channel_buffer
			