from network.channel_buffer import ChannelBuffer
from protocol.protocol_pb2 import StartServerInitRequest
from master_server.global_data import GlobalData

class StartServerInitRequestHandler:
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		print channel_name
		print message_id
		print channel_buffer
		message = StartServerInitRequest.FromString(channel_buffer.read_all_data())
		print message.name

		global_data.server_manager.add_server(message.name)