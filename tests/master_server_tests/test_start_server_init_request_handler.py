import unittest
import tests.auxiliary
from master_server.start_server_init_request_handler import StartServerInitRequestHandler
import protocol.protocol_message_pb2
from common.server_type import ServerType
from network.channel_buffer import ChannelBuffer
from mock import Mock
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from protocol.protocol_id import ProtocolID

class StartServerInitRequestHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = StartServerInitRequestHandler()

	def test_handle_message(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = 'sa'
		message.type = ServerType.AUTHENTICATION_SERVER
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		global_data.rmq = Mock()
		global_data.rmq.send_message_string = Mock()
		
		message_to_send = protocol.protocol_message_pb2.StartServerInitResponse()
		
		self.handler.handle_message(global_data, 'test_channel', 1, channel_buffer)
		
		self.assertEqual(len(global_data.server_manager.servers), 1)
		global_data.rmq.send_message_string.assert_called_with(message_to_send, 'sa', ProtocolID.START_SERVER_INIT_RESPONSE)
		
def get_tests():
	return unittest.makeSuite(StartServerInitRequestHandlerTest)

if '__main__' == __name__:
	unittest.main()