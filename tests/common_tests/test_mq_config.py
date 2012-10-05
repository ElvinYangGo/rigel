import unittest
import tests.auxiliary
from mock import Mock
from common.mq_config import MQConfig

class MqConfigTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_init(self):
		config_string = '{"pub_address": "localhost:34510", "sub_address": "localhost:34511"}'
		mq_config = MQConfig(config_string=config_string)
		self.assertEqual(mq_config.get_pub_address(), "localhost:34510")
		self.assertEqual(mq_config.get_sub_address(), "localhost:34511")

def get_tests():
	return unittest.makeSuite(MqConfigTest)

if '__main__' == __name__:
	unittest.main()