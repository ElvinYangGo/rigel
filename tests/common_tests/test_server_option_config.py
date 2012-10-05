import unittest
import tests.auxiliary
from mock import Mock
from common.server_option_config import ServerOptionConfig

class ServerOptionConfigTest(unittest.TestCase):
	def setUp(self):
		self.config_string = '{"heart_beat_alive": 15000, "heart_beat_timeout": 60000, "heart_beat_interval": 10000}'
		self.server_option_config = ServerOptionConfig(config_string=self.config_string)

	def test_init(self):
		self.assertNotEqual(self.server_option_config.config, None)

	def test_get_heart_beat_interval(self):
		self.assertEqual(self.server_option_config.get_heart_beat_interval(), 10000)

	def test_to_json_string(self):
		self.assertEqual(self.server_option_config.to_json_string(), self.config_string)

def get_tests():
	return unittest.makeSuite(ServerOptionConfigTest)

if '__main__' == __name__:
	unittest.main()