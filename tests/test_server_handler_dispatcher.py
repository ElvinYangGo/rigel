import unittest
import tests.auxiliary
from mock import Mock
from common.server_handler_dispatcher import ServerHandlerDispatcher
from network.channel_buffer import ChannelBuffer

class ServerHandlerDispatcherTest(unittest.TestCase):
	def setUp(self):
		self.server_handler_dispatcher = ServerHandlerDispatcher()
		
	def testHandleUpstream(self):
		channel_buffer = ChannelBuffer()
		channel_buffer.write_int(111)
		handler = Mock()
		handler.handle_message = Mock()
		global_data = Mock()
		self.server_handler_dispatcher.append_handler(111, handler)
		channel_name = 'test_name'
		self.server_handler_dispatcher.handle_upstream(global_data, channel_name, channel_buffer)
		handler.handle_message.assert_called_with(global_data, channel_name, 111, channel_buffer)
		self.assertEqual(0, channel_buffer.readable_bytes())
		
	def testHandleUpstream2(self):		
		channel_buffer = ChannelBuffer()
		channel_buffer.write_int(112)
		handler = Mock()
		handler.handle_message = Mock()
		global_data = Mock()
		self.server_handler_dispatcher.append_handler(111, handler)
		channel_name = 'test_name'
		self.server_handler_dispatcher.handle_upstream(global_data, channel_name, channel_buffer)
		self.assertFalse(handler.handle_message.called)
		self.assertEqual(4, channel_buffer.readable_bytes())
	
	
def get_tests():
	return unittest.makeSuite(ServerHandlerDispatcherTest)

if '__main__' == __name__:
	unittest.main()