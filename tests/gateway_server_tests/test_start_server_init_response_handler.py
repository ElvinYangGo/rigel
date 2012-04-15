import unittest
import tests.auxiliary
from mock import Mock
import protocol.protocol_message_pb2
from protocol.protocol_id import ProtocolID
from gateway_server.start_server_init_response_handler import StartServerInitResponseHandler

class StartServerInitResponseHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = StartServerInitResponseHandler()
	
	def test_handle_message(self):
		global_data = Mock()
		global_data.rmq = Mock()
		global_data.rmq.subscribe = Mock()
		global_data.rmq.send_message_string = Mock()
		global_data.server_name = u'gateway_server'
		channel_buffer = Mock()
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = u'gateway_server'	
		
		self.handler.handle_message(global_data, u'test_channel', ProtocolID.START_SERVER_INIT_RESPONSE, channel_buffer)
		
		global_data.rmq.subscribe.assert_called_with(u'server_status')
		global_data.rmq.send_message_string.assert_called_with(message, u'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
		
def get_tests():
	return unittest.makeSuite(StartServerInitResponseHandlerTest)

if '__main__' == __name__:
	unittest.main()