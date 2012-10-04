import unittest
import tests.auxiliary
from mock import Mock
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.server_type import ServerType
from center_server.center_server_initializer import CenterServerInitializer
from common.global_data import GlobalData
from center_server.center_global_data import CenterGlobalData
from common.server_initializer import ServerInitializer
from common.channel_name import ChannelName

class CenterServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_name = u'center_server'
		GlobalData.inst = CenterGlobalData()
		self.server_initializer = CenterServerInitializer(
			'localhost:34510',
			'localhost:34511', 
			self.server_name,
			Mock(),
			Mock(),
			Mock()
			)
		
	def test_init_global_data(self):
		ServerInitializer.init_global_data = Mock()
		self.server_initializer.init_global_data()
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 0)
		self.assertEqual(GlobalData.inst.server_name, self.server_name)
		
	def test_send_init_request(self):
		self.server_initializer.rmq = Mock()
		self.server_initializer.rmq.send_message_string = Mock()
		GlobalData.inst.server_name = self.server_name
		self.server_initializer.send_init_request()
		
		message = protocol.server_message_pb2.StartServerInitReq()
		message.name = self.server_name
		message.type = ServerType.CENTER_SERVER
		self.server_initializer.rmq.send_message.assert_called_with(
			message,
			ChannelName.SERVER_INIT,
			ServerProtocolID.P_START_SERVER_INIT_REQ
			)

def get_tests():
	return unittest.makeSuite(CenterServerInitializerTest)

if '__main__' == __name__:
	unittest.main()