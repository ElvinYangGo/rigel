import unittest
import tests.auxiliary
from common.start_server_init_response_handler import StartServerInitResponseHandler
from common.server_option_reader import ServerOptionReader

class StartServerInitResponseHandlerTest(unittest.TestCase):
	def setUp(self):
		self.start_server_init_response_handler = StartServerInitResponseHandler()
		self.config = u'<config><server_option_config><config><heart_beat_interval>10000</heart_beat_interval><heart_beat_timeout>120000</heart_beat_timeout></config></server_option_config></config>'
		"""
		<config>
			<server_option_config>
				<config>
					<heart_beat_interval>10000</heart_beat_interval>
					<heart_beat_timeout>120000</heart_beat_timeout>
				</config>
			</server_option_config>
		</config>
		"""
		
	def test_has_config(self):
		self.assertTrue(self.start_server_init_response_handler.has_config(self.config, u'server_option_config'))
		self.assertFalse(self.start_server_init_response_handler.has_config(self.config, u'invalid_config'))
		
	def test_get_config_string(self):
		server_option_config_string = self.start_server_init_response_handler.get_config_string(self.config, u'server_option_config')
		server_option_reader = ServerOptionReader(string_content=server_option_config_string)
		server_option_reader.parse()
		self.assertEqual(server_option_reader.get_server_option_config().get_heart_beat_interval(), 10000)
		
	def test_get_server_option_reader(self):
		server_option_reader = self.start_server_init_response_handler.get_server_option_reader(self.config)
		self.assertEqual(server_option_reader.get_server_option_config().get_heart_beat_interval(), 10000)

def get_tests():
	return unittest.makeSuite(StartServerInitResponseHandlerTest)

if '__main__' == __name__:
	unittest.main()