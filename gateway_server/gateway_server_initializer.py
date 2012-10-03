from gateway_server.gateway_global_data import GatewayGlobalData
from common.server_initializer import ServerInitializer
from protocol.server_protocol_id import ServerProtocolID
from common.server_manager import ServerManager
import protocol.server_message_pb2
from common.server_type import ServerType
from network.channel_manager import ChannelManager
from mq_client.rmq_pub import RMQPub
from common.global_data import GlobalData

class GatewayServerInitializer(ServerInitializer):
	def __init__(
		self,
		pub_address,
		sub_address,
		server_name,
		pipeline,
		redis_server_file_name,
		redis_partition_file_name
		):
		super(GatewayServerInitializer, self).__init__(
			pub_address,
			sub_address,
			server_name,
			pipeline,
			redis_server_file_name,
			redis_partition_file_name
			)
	
	def init_global_data(self):
		GlobalData.inst = GatewayGlobalData()
		super(GatewayServerInitializer, self).init_global_data()
		GlobalData.inst.server_manager = ServerManager()
		GlobalData.inst.server_name = self.server_name
		GlobalData.inst.channel_manager = ChannelManager()
	
	def init_rmq(self):
		super(GatewayServerInitializer, self).init_rmq()
		rmq_pub = RMQPub(self.pub_address, GlobalData.inst.zmq_context, self.pipeline)
		GlobalData.inst.rmq_pub = rmq_pub

	def send_init_request(self):
		message = protocol.server_message_pb2.StartServerInitReq()
		message.name = GlobalData.inst.server_name
		message.type = ServerType.GATEWAY_SERVER
		self.rmq.send_message(
			message, u'server_initialization', ServerProtocolID.P_START_SERVER_INIT_REQ
			)

