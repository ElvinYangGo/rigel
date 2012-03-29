class ServerHandlerDispatcher:
	def __init__(self):
		self.handlers = {}
		
	def append_handler(self, key, handler):
		self.handlers[key] = handler
		
	def handle_upstream(self, global_data, channel_name, channel_buffer):
		message_id = channel_buffer.get_int()
		if self.handlers.has_key(message_id):
			channel_buffer.skip_data(4)
			handler = self.handlers.get(message_id)
			handler.handle_message(global_data, channel_name, message_id, channel_buffer)
		else:
			#send to upstream
			return channel_buffer
	