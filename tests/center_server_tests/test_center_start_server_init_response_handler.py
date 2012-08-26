import unittest
import tests.auxiliary
from mock import Mock
import protocol.protocol_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from center_server.center_start_server_init_res_handler import CenterStartServerInitResHandler
from network.channel_buffer import ChannelBuffer
from common.global_data import GlobalData

class CenterStartServerInitResponseHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = CenterStartServerInitResHandler()
	
	def test_handle_message(self):
		GlobalData.instance = Mock()
		GlobalData.instance.rmq = Mock()
		GlobalData.instance.rmq.subscribe = Mock()
		GlobalData.instance.rmq.send_message_string = Mock()
		GlobalData.instance.server_name = u'center_server'
		
		m = protocol.protocol_message_pb2.StartServerInitRes()
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
		
		message = protocol.protocol_message_pb2.EndServerInitNotice()
		message.name = u'center_server'		
	
		self.handler.handle_message(
			ServerProtocolID.P_START_SERVER_INIT_RES, channel_buffer, channel_name=u'test_channel'
			)
		
		GlobalData.instance.rmq.subscribe.assert_called_with(u'server_status')
		GlobalData.instance.rmq.send_message_string.assert_called_with(
			message, u'server_initialization', ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
		self.assertTrue(self.handler.init_heart_beat.called)
		
def get_tests():
	return unittest.makeSuite(CenterStartServerInitResponseHandlerTest)

if '__main__' == __name__:
	unittest.main()