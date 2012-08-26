from common.server_initializer import ServerInitializer
from protocol.server_protocol_id import ServerProtocolID
from common.server_manager import ServerManager
import protocol.server_message_pb2
from common.server_type import ServerType
from common.global_data import GlobalData
from auth_server.auth_global_data import AuthGlobalData

class AuthServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, pipeline):
		super(AuthServerInitializer, self).__init__(pub_address, sub_address, server_name, pipeline)
	
	def init_global_data(self):
		GlobalData.instance = AuthGlobalData()
		super(AuthServerInitializer, self).init_global_data()
		GlobalData.instance.server_manager = ServerManager()
		GlobalData.instance.server_name = self.server_name
	
	def send_init_request(self):
		message = protocol.server_message_pb2.StartServerInitReq()
		message.name = GlobalData.instance.server_name
		message.type = ServerType.AUTHENTICATION_SERVER
		self.rmq.send_message_string(message, u'server_initialization', ServerProtocolID.P_START_SERVER_INIT_REQ)

