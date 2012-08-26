from gateway_server.gateway_global_data import GatewayGlobalData
from common.server_initializer import ServerInitializer
from protocol.server_protocol_id import ServerProtocolID
from common.server_manager import ServerManager
import protocol.protocol_message_pb2
from common.server_type import ServerType
from network.channel_manager import ChannelManager
from mq_client.rmq_pub import RMQPub
from common.global_data import GlobalData

class GatewayServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, pipeline):
		super(GatewayServerInitializer, self).__init__(pub_address, sub_address, server_name, pipeline)
	
	def init_global_data(self):
		GlobalData.instance = GatewayGlobalData()
		super(GatewayServerInitializer, self).init_global_data()
		GlobalData.instance.server_manager = ServerManager()
		GlobalData.instance.server_name = self.server_name
		GlobalData.instance.channel_manager = ChannelManager()
	
	def init_rmq(self):
		super(GatewayServerInitializer, self).init_rmq()
		rmq_pub = RMQPub(self.pub_address, GlobalData.instance.zmq_context)
		GlobalData.instance.rmq_pub = rmq_pub

	def send_init_request(self):
		message = protocol.protocol_message_pb2.StartServerInitReq()
		message.name = GlobalData.instance.server_name
		message.type = ServerType.GATEWAY_SERVER
		self.rmq.send_message_string(
			message, u'server_initialization', ServerProtocolID.P_START_SERVER_INIT_REQ
			)

