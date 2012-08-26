import unittest
import tests.auxiliary
from mock import Mock
import protocol.server_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from network.channel_buffer import ChannelBuffer
from gateway_server.gateway_start_server_init_res_handler import GatewayStartServerInitResHandler
from common.global_data import GlobalData

class GatewayStartServerInitResponseHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = GatewayStartServerInitResHandler()
	
	def test_handle_message(self):
		GlobalData.instance = Mock()
		GlobalData.instance.rmq.subscribe = Mock()
		GlobalData.instance.rmq.send_message_string = Mock()
		GlobalData.instance.server_name = u'gateway_server'
		
		m = protocol.server_message_pb2.StartServerInitRes()
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
		
		message = protocol.server_message_pb2.EndServerInitNotice()
		message.name = u'gateway_server'	
		
		self.handler.handle_message(
			ServerProtocolID.P_START_SERVER_INIT_RES, channel_buffer, channel_name=u'test_channel'
			)
		
		GlobalData.instance.rmq.subscribe.assert_called_with(u'server_status')
		GlobalData.instance.rmq.send_message_string.assert_called_with(
			message, u'server_initialization', ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
		self.assertTrue(self.handler.init_heart_beat.called)
		
def get_tests():
	return unittest.makeSuite(GatewayStartServerInitResponseHandlerTest)

if '__main__' == __name__:
	unittest.main()