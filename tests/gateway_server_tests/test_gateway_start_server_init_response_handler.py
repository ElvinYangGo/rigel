import unittest
import tests.auxiliary
from mock import Mock
import protocol.protocol_message_pb2
from protocol.protocol_id import ProtocolID
from network.channel_buffer import ChannelBuffer
from gateway_server.gateway_start_server_init_response_handler import GatewayStartServerInitResponseHandler

class GatewayStartServerInitResponseHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = GatewayStartServerInitResponseHandler()
	
	def test_handle_message(self):
		global_data = Mock()
		global_data.rmq = Mock()
		global_data.rmq.subscribe = Mock()
		global_data.rmq.send_message_string = Mock()
		global_data.server_name = u'gateway_server'
		
		m = protocol.protocol_message_pb2.StartServerInitResponse()
		m.config = u"""
		<config>
			<server_option_config>
				<config>
					<heart_beat_interval>10000</heart_beat_interval>
					<heart_beat_timeout>120000</heart_beat_timeout>
				</config>
			</server_option_config>
		</config>
		"""
		channel_buffer = ChannelBuffer(m.SerializeToString())
		self.handler.init_heart_beat = Mock()
		
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = u'gateway_server'	
		
		self.handler.handle_message(global_data, u'test_channel', ProtocolID.START_SERVER_INIT_RESPONSE, channel_buffer)
		
		global_data.rmq.subscribe.assert_called_with(u'server_status')
		global_data.rmq.send_message_string.assert_called_with(message, u'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
		self.assertTrue(self.handler.init_heart_beat.called)
		
def get_tests():
	return unittest.makeSuite(GatewayStartServerInitResponseHandlerTest)

if '__main__' == __name__:
	unittest.main()