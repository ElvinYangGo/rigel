import unittest
import tests.auxiliary
from common.start_server_init_res_handler import StartServerInitResHandler
from mock import Mock
from common.global_data import GlobalData
import protocol.server_message_pb2
from network.channel_buffer import ChannelBuffer
from protocol.server_protocol_id import ServerProtocolID
from common.channel_name import ChannelName

class StartServerInitResHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = StartServerInitResHandler()

	def test_handle_message(self):
		GlobalData.inst = Mock()
		GlobalData.inst.rmq = Mock()
		GlobalData.inst.rmq.subscribe = Mock()
		GlobalData.inst.rmq.send_message_string = Mock()
		GlobalData.inst.server_name = u'auth_server'

		m = protocol.server_message_pb2.StartServerInitRes()
		m.config = u'{"server_option_config": "{\\"heart_beat_timeout\\": 60000, \\"heart_beat_interval\\": 10000}"}'
		channel_buffer = ChannelBuffer(m.SerializeToString())
		self.handler.init_heart_beat = Mock()

		message = protocol.server_message_pb2.EndServerInitNotice()
		message.name = u'auth_server'

		self.handler.handle_message(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			channel_buffer,
			channel_name=u'test_channel'
			)

		GlobalData.inst.rmq.subscribe.assert_called_with(ChannelName.SERVER_STATUS)
		GlobalData.inst.rmq.send_message.assert_called_with(
			message,
			ChannelName.SERVER_INIT,
			ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
		self.assertTrue(self.handler.init_heart_beat.called)

def get_tests():
	return unittest.makeSuite(StartServerInitResHandlerTest)

if '__main__' == __name__:
	unittest.main()