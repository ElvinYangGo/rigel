import unittest
import tests.auxiliary
from common.mq_reader import MQReader

class MqReaderTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_parse(self):
		xml_string = """<?xml version="1.0" encoding="utf-8"?>
		<config>
			<mq>
				<pub_address>localhost:34510</pub_address>
				<sub_address>localhost:34511</sub_address>
			</mq>
		</config>
		"""
		mq_reader = MQReader(string_content=xml_string)
		mq_reader.parse()
		self.assertEqual(len(mq_reader.get_mq_config_list()), 1)
		self.assertEqual(mq_reader.get_mq_config_list()[0].get_pub_address(), 'localhost:34510')
		self.assertEqual(mq_reader.get_mq_config_list()[0].get_sub_address(), 'localhost:34511')

def get_tests():
	return unittest.makeSuite(MqReaderTest)

if '__main__' == __name__:
	unittest.main()
