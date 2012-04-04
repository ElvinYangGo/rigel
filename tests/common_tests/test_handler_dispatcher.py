import unittest
import tests.auxiliary
from mock import Mock
from common.handler_dispatcher import HandlerDispatcher
from network.channel_buffer import ChannelBuffer

class HandlerDispatcherTest(unittest.TestCase):
	def setUp(self):
		self.handler_dispatcher = HandlerDispatcher()

	def test_handle_connection(self):
		handler = Mock()
		handler.handle_connection = Mock()
		channel = Mock()
		self.handler_dispatcher.append_handler(1, handler)
		self.handler_dispatcher.handle_connection(channel)
		handler.handle_connection.assert_called_with(channel)
		
	def test_handle_disconnection(self):
		handler = Mock()
		handler.handle_disconnection = Mock()
		channel = Mock()
		self.handler_dispatcher.append_handler(1, handler)
		self.handler_dispatcher.handle_disconnection(channel)
		handler.handle_disconnection.assert_called_with(channel)
		
	def test_handle_upstream_with_return(self):
		handler = Mock()
		handler.handle_message = Mock()
		channel = Mock()
		channel_buffer = ChannelBuffer()
		channel_buffer.write_int(1)
		self.handler_dispatcher.append_handler(1, handler)
		self.handler_dispatcher.handle_upstream(channel, channel_buffer)
		handler.handle_message.assert_called_with(1, channel, channel_buffer)
		self.assertEqual(0, channel_buffer.readable_bytes())
		
	def test_handle_upstream_without_return(self):
		handler = Mock()
		handler.handle_message = Mock()
		channel = Mock()
		channel_buffer = ChannelBuffer()
		channel_buffer.write_int(2)
		self.handler_dispatcher.append_handler(1, handler)
		self.handler_dispatcher.handle_upstream(channel, channel_buffer)
		self.assertFalse(handler.handle_message.called)
		self.assertEqual(4, channel_buffer.readable_bytes())
		
def get_tests():
	return unittest.makeSuite(HandlerDispatcherTest)

if '__main__' == __name__:
	unittest.main()