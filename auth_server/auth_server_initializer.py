from common.server_initializer import ServerInitializer
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.server_type import ServerType
from common.global_data import GlobalData
from auth_server.auth_global_data import AuthGlobalData
from auth_server.gateway_address import GatewayAddress
from auth_server.auth_server_manager import AuthServerManager

class AuthServerInitializer(ServerInitializer):
	def __init__(
		self,
		pub_address,
		sub_address,
		server_name,
		pipeline,
		redis_server_file_name, 
		redis_partition_file_name,
		gateway_address_file_name
		):
		super(AuthServerInitializer, self).__init__(
			pub_address,
			sub_address,
			server_name,
			pipeline,
			redis_server_file_name,
			redis_partition_file_name
			)
		self.gateway_address_file_name = gateway_address_file_name
	
	def init_global_data(self):
		GlobalData.inst = AuthGlobalData()
		super(AuthServerInitializer, self).init_global_data()
		GlobalData.inst.server_manager = AuthServerManager()
		GlobalData.inst.server_name = self.server_name
		GlobalData.inst.gateway_address = GatewayAddress(self.gateway_address_file_name)
	
	def send_init_request(self):
		message = protocol.server_message_pb2.StartServerInitReq()
		message.name = GlobalData.inst.server_name
		message.type = ServerType.AUTHENTICATION_SERVER
		self.rmq.send_message(message, u'server_initialization', ServerProtocolID.P_START_SERVER_INIT_REQ)

