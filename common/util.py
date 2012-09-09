def send_result(channel, message, protocol_id, error_code):
	message.result = error_code
	channel.send_string(message.SerializeToString(), protocol_id)