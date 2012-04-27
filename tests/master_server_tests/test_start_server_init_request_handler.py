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
from common.server_option_reader import ServerOptionReader

class StartServerInitRequestHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = StartServerInitRequestHandler()

	def test_handle_message(self):
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = u'sa'
		message.type = ServerType.AUTHENTICATION_SERVER
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		global_data.rmq = Mock()
		global_data.rmq.send_message_string = Mock()
		
		message_to_send = protocol.protocol_message_pb2.StartServerInitResponse()
		message_to_send.config = ''
		
		self.handler.create_config_xml_string = Mock()
		self.handler.create_config_xml_string.return_value = ''
		self.handler.handle_message(global_data, u'test_channel', 1, channel_buffer)
		
		self.assertEqual(len(global_data.server_manager.servers), 1)
		global_data.rmq.send_message_string.assert_called_with(message_to_send, u'sa', ProtocolID.START_SERVER_INIT_RESPONSE)
		
	def test_config_xml_string(self):
		content = u"""<config><heart_beat_interval>10000</heart_beat_interval><heart_beat_timeout>120000</heart_beat_timeout></config>"""
		"""
		<config>
			<heart_beat_interval>10000</heart_beat_interval>
			<heart_beat_timeout>120000</heart_beat_timeout>
		</config>
		"""
		
		global_data = GlobalData()
		global_data.server_option_reader = ServerOptionReader(string_content=content)
		global_data.server_option_reader.parse()
		config_xml_string = self.handler.create_config_xml_string(global_data)
		
		config_should_be = u'<?xml version="1.0" encoding="utf-8"?><config><server_option_config><config><heart_beat_interval>10000</heart_beat_interval><heart_beat_timeout>120000</heart_beat_timeout></config></server_option_config></config>'
		self.assertEqual(config_xml_string, config_should_be)
		
def get_tests():
	return unittest.makeSuite(StartServerInitRequestHandlerTest)

if '__main__' == __name__:
	unittest.main()