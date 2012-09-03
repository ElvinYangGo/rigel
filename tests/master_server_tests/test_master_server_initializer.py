import unittest
from mock import Mock
import tests.auxiliary
from master_server.master_server_initializer import MasterServerInitializer
from master_server.master_global_data import MasterGlobalData
from common.global_data import GlobalData
from common.server_initializer import ServerInitializer

class MasterServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_name = u'master_server'
		GlobalData.inst = MasterGlobalData()
		self.server_option_reader = Mock()
		self.server_initializer = MasterServerInitializer(
			'localhost:34510', 
			'localhost:34511',
			self.server_name,
			Mock(),
			Mock(),
			Mock(),
			self.server_option_reader
			)
		self.server_initializer.init_heart_beat_monitor = Mock()
		
	def test_construction(self):
		self.assertEqual(self.server_initializer.server_option_reader, self.server_option_reader)
		
	def test_init_global_data(self):
		ServerInitializer.init_global_data = Mock()
		self.server_initializer.init_global_data()
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 0)
		self.assertEqual(GlobalData.inst.server_option_reader, self.server_option_reader)
		self.assertTrue(self.server_initializer.init_heart_beat_monitor.called)
		
def get_tests():
	return unittest.makeSuite(MasterServerInitializerTest)

if '__main__' == __name__:
	unittest.main()