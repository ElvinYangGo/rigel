from protocol.protocol_id import ProtocolID
from network.channel_buffer import ChannelBuffer
import protocol.protocol_pb2

class StartServerInitResponseHandler:
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		print channel_name
		print message_id
		print channel_buffer

		global_data.rmq.subscribe('server_status')
		message = protocol.protocol_pb2.EndServerInitNotification()
		message.name = 'authentication_server'		
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message.SerializeToString())
		global_data.rmq.send(channel_buffer, 'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
