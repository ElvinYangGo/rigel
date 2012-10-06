import unittest
import tests.auxiliary
from auth_server.auth_server_initializer import AuthServerInitializer
from mock import Mock
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.server_type import ServerType
from common.global_data import GlobalData
from auth_server.auth_global_data import AuthGlobalData
from common.server_initializer import ServerInitializer
import auth_server.auth_server_initializer
from common.channel_name import ChannelName

class AuthServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_name = u'auth_server'
		GlobalData.inst = AuthGlobalData()
		self.server_initializer = AuthServerInitializer(
			'localhost:34510',
			'localhost:34511',
			self.server_name,
			'a',
			'b',
			'c',
			'd',
			'e'
			)
		
	def test_init_global_data(self):
		ServerInitializer.init_global_data = Mock()
		auth_server.auth_server_initializer.GatewayAddress = Mock()
		auth_server.auth_server_initializer.GatewayAddress.return_value = Mock()
		self.server_initializer.init_global_data()
		self.assertNotEqual(GlobalData.inst.server_manager, None)
		self.assertEqual(
			GlobalData.inst.gateway_address,
			auth_server.auth_server_initializer.GatewayAddress.return_value
			)

	def test_send_init_request(self):
		self.server_initializer.rmq = Mock()
		self.server_initializer.rmq.send_message_string = Mock()
		GlobalData.inst.server_name = self.server_name
		self.server_initializer.send_init_request()
		
		message = protocol.server_message_pb2.InitServerReq()
		message.name = self.server_name
		message.type = ServerType.AUTH_SERVER
		self.server_initializer.rmq.send_message.assert_called_with(
			message,
			ChannelName.SERVER_INIT,
			ServerProtocolID.P_INIT_SERVER_REQ
			)

def get_tests():
	return unittest.makeSuite(AuthServerInitializerTest)

if '__main__' == __name__:
	unittest.main()