class ClientMessageRelay:
	def handle_upstream(self, channel, channel_buffer):
		message_id = channel_buffer.get_int()
		#TODO
		#send to mq
	
