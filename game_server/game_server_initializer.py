from common.server_initializer import ServerInitializer
from protocol.protocol_id import ProtocolID
from common.server_manager import ServerManager
import protocol.protocol_message_pb2
from common.server_type import ServerType
from game_server.game_global_data import GameGlobalData
from common.global_data import GlobalData

class GameServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, pipeline):
		super(GameServerInitializer, self).__init__(pub_address, sub_address, server_name, pipeline)

	def init_global_data(self):
		GlobalData.instance = GameGlobalData()
		super(GameServerInitializer, self).init_global_data()
		GlobalData.instance.server_manager = ServerManager()
		GlobalData.instance.server_name = self.server_name
	
	def send_init_request(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = GlobalData.instance.server_name
		message.type = ServerType.GAME_SERVER
		self.rmq.send_message_string(message, u'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

