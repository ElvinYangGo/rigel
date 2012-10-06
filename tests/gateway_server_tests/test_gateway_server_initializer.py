import unittest
import tests.auxiliary
from mock import Mock
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.server_type import ServerType
from gateway_server.gateway_server_initializer import GatewayServerInitializer
from gateway_server.gateway_global_data import GatewayGlobalData
from common.global_data import GlobalData
from common.server_initializer import ServerInitializer
from common.channel_name import ChannelName

class GameServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_name = u'gateway_server'
		GlobalData.inst = GatewayGlobalData()
		self.server_initializer = GatewayServerInitializer(
			'localhost:34510',
			'localhost:34511',
			self.server_name,
			'a',
			'b',
			'c',
			'd'
			)
		
	def test_init_global_data(self):
		ServerInitializer.init_global_data = Mock()
		self.server_initializer.init_global_data()
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 0)
		self.assertEqual(len(GlobalData.inst.channel_manager.channels), 0)
		
	def test_send_init_request(self):
		self.server_initializer.rmq = Mock()
		self.server_initializer.rmq.send_message_string = Mock()
		GlobalData.inst.server_name = self.server_name
		self.server_initializer.send_init_request()
		
		message = protocol.server_message_pb2.InitServerReq()
		message.name = self.server_name
		message.type = ServerType.GATEWAY_SERVER
		self.server_initializer.rmq.send_message.assert_called_with(
			message,
			ChannelName.SERVER_INIT,
			ServerProtocolID.P_INIT_SERVER_REQ
			)

def get_tests():
	return unittest.makeSuite(GameServerInitializerTest)

if '__main__' == __name__:
	unittest.main()