from network.channel_buffer import ChannelBuffer
import protocol.protocol_pb2
from master_server.global_data import GlobalData
from network.channel_buffer import ChannelBuffer
from protocol.protocol_id import ProtocolID

class StartServerInitRequestHandler:
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		print channel_name
		print message_id
		print channel_buffer
		message = protocol.protocol_pb2.StartServerInitRequest.FromString(channel_buffer.read_all_data())
		print message.name

		global_data.server_manager.add_server(message.name, message.type)
		
		message_to_send = protocol.protocol_pb2.StartServerInitResponse()
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message_to_send.SerializeToString())
		global_data.rmq.send(channel_buffer, 'server_initialization', ProtocolID.START_SERVER_INIT_RESPONSE)
