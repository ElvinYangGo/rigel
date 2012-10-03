import unittest
import tests.auxiliary
from mock import Mock
from network.channel_buffer import ChannelBuffer
from common.protocol_wrapper_handler import ProtocolWrapperHandler
import protocol.server_message_pb2

class ProtocolWrapperHandlerTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_handle_downstream(self):
		channel_buffer = 'aaa'
		protocol_wrapper_handler = ProtocolWrapperHandler(Mock())
		buffer_to_check = protocol_wrapper_handler.handle_downstream(channel_buffer)
		self.assertEqual(buffer_to_check, channel_buffer)

		buffer_to_check = protocol_wrapper_handler.handle_downstream(channel_buffer, inner_message_id=0x5001)
		self.assertEqual(buffer_to_check, channel_buffer)

		protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper()
		protocol_wrapper.protocol_id = 0x1001
		protocol_wrapper.client_conn_info.client_id = 1
		protocol_wrapper.inner_protocol = 'aaa'
		channel_buffer = ChannelBuffer(protocol_wrapper.SerializeToString())
		buffer_to_check = protocol_wrapper_handler.handle_downstream(
			ChannelBuffer('aaa'), inner_message_id=0x1001, client_id=1
			)
		self.assertEqual(buffer_to_check.get_all_data(), channel_buffer.get_all_data())

def get_tests():
	return unittest.makeSuite(ProtocolWrapperHandlerTest)

if '__main__' == __name__:
	unittest.main()