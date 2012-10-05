import unittest
import tests.auxiliary
from mock import Mock
from common.server_initializer import ServerInitializer
from common.global_data import GlobalData

class ServerInitializerTest(unittest.TestCase):
	def setUp(self):
		GlobalData.inst = GlobalData()
		self.channel_pipeline = Mock()
		self.server_name = u'auth_server'
		self.server_initializer = ServerInitializer(
			'localhost:34510',
			'localhost:34511', 
			self.server_name,
			self.channel_pipeline,
			Mock(),
			Mock()
			)
		
	def test_construction(self):
		self.assertEqual(self.server_initializer.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.sub_address, 'localhost:34511')
		self.assertEqual(self.server_initializer.server_name, self.server_name)
		
def get_tests():
	return unittest.makeSuite(ServerInitializerTest)

if '__main__' == __name__:
	unittest.main()