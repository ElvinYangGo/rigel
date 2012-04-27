import unittest
import tests.auxiliary
from common.server_option_reader import ServerOptionReader

class ServerOptionReaderTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_parse(self):
		content = u"""<config><heart_beat_interval>10000</heart_beat_interval><heart_beat_timeout>120000</heart_beat_timeout></config>"""
		"""
		<config>
			<heart_beat_interval>10000</heart_beat_interval>
			<heart_beat_timeout>120000</heart_beat_timeout>
		</config>
		"""
		server_option_reader = ServerOptionReader(string_content=content)
		self.assertTrue(server_option_reader.get_xml_string() is None)
		server_option_reader.parse()
		self.assertEqual(server_option_reader.get_server_option_config().get_heart_beat_interval(), 10000)
		self.assertEqual(server_option_reader.get_server_option_config().get_heart_beat_timeout(), 120000)
		self.assertEqual(server_option_reader.get_xml_string(), content)
		
def get_tests():
	return unittest.makeSuite(ServerOptionReaderTest)

if '__main__' == __name__:
	unittest.main()