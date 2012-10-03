import unittest
import tests.auxiliary
from mock import Mock
from gateway_server.server_message_relay import ServerMessageRelay
from gateway_server.gateway_global_data import GatewayGlobalData
import protocol.server_message_pb2
from network.channel_buffer import ChannelBuffer

class ServerMessageRelayTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_handle_upstream(self):
		protocol_wrapper = protocol.server_message_pb2.ProtocolWrapper()
		protocol_wrapper.client_conn_info.client_id = 1
		protocol_wrapper.inner_protocol = 'aaa'
		protocol_wrapper.protocol_id = 1
		channel_buffer = ChannelBuffer(protocol_wrapper.SerializeToString())
		channel = Mock()
		channel.send_string = Mock()
		GatewayGlobalData.inst = Mock()
		GatewayGlobalData.inst.channel_manager.get_channel.return_value = channel

		server_message_relay = ServerMessageRelay()
		server_message_relay.handle_upstream(channel_buffer)
		GatewayGlobalData.inst.channel_manager.get_channel.assert_called_with(1)
		channel.send_string.assert_called_with('aaa', 1)

def get_tests():
	return unittest.makeSuite(ServerMessageRelayTest)

if '__main__' == __name__:
	unittest.main()