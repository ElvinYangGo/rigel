from common.server_initializer import ServerInitializer
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID
from authentication_server.start_server_init_response_handler import StartServerInitResponseHandler
from authentication_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler
from authentication_server.global_data import GlobalData
from authentication_server.server_manager import ServerManager
import protocol.protocol_message_pb2
from common.server_type import ServerType
from network.channel_buffer import ChannelBuffer
from mq_client.rmq import RMQ

class AuthenticationServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address):
		self.pub_address = pub_address
		self.sub_address = sub_address
		self.server_handler_dispatcher = None
		self.global_data = None
		self.rmq = None
		
	def init_server_handler_dispatcher(self):
		self.server_handler_dispatcher = ServerHandlerDispatcher()
		self.server_handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_RESPONSE,
			StartServerInitResponseHandler()
			)
		self.server_handler_dispatcher.append_handler(
			ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
			SynchronizeServerStatusNotificationHandler()
			)
	
		return self.server_handler_dispatcher
		def init_global_data(self):
		self.global_data = GlobalData()
		self.global_data.server_manager = ServerManager()
		return self.global_data
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, self.server_handler_dispatcher)
		self.rmq.subscribe('server_initialization')
	
		self.global_data.rmq = self.rmq
		self.rmq.set_global_data(self.global_data)
	
		self.rmq.start()

	def send_init_request(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = 'authentication_server'		
		message.type = ServerType.AUTHENTICATION_SERVER
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message.SerializeToString())
		self.rmq.send(channel_buffer, 'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

