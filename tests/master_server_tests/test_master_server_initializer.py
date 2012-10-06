import unittest
from mock import Mock
import tests.auxiliary
from master_server.master_server_initializer import MasterServerInitializer
from master_server.master_global_data import MasterGlobalData
from common.global_data import GlobalData
from common.server_initializer import ServerInitializer
import master_server.master_server_initializer
from common.server_status import ServerStatus

class MasterServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_name = u'master_server'
		GlobalData.inst = MasterGlobalData()
		self.server_option_reader = Mock()
		self.server_initializer = MasterServerInitializer(
			'localhost:34510', 
			'localhost:34511',
			self.server_name,
			'a',
			'b',
			'c',
			'd'
			)
		
	def test_init_global_data(self):
		ServerInitializer.init_global_data = Mock()
		self.server_initializer.init_global_data()
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 0)
		self.assertEqual(GlobalData.inst.server_status, ServerStatus.SERVER_STATUS_RUNNING)

	def test_init_heart_beat_monitor(self):
		GlobalData.inst.server_option_config = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_interval = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_interval.return_value = 1
		GlobalData.inst.server_option_config.get_heart_beat_timeout = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_timeout.return_value = 2
		GlobalData.inst.server_option_config.get_heart_beat_alive = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_alive.return_value = 3
		master_server.master_server_initializer.HeartBeatMonitor = Mock()
		master_server.master_server_initializer.HeartBeatMonitor.return_value = Mock()
		master_server.master_server_initializer.HeartBeatMonitor.return_value.start = Mock()

		self.server_initializer.init_heart_beat_monitor()

		master_server.master_server_initializer.HeartBeatMonitor.assert_called_with(
			1, 2, 3
			)
		self.assertTrue(master_server.master_server_initializer.HeartBeatMonitor.return_value.start.called)
	def init_heart_beat_monitor(self):
		heart_beat_interval = GlobalData.inst.server_option_config.get_heart_beat_interval()
		heart_beat_timeout = GlobalData.inst.server_option_config.get_heart_beat_timeout()
		heart_beat_alive = GlobalData.inst.server_option_config.get_heart_beat_alive()
		GlobalData.inst.heart_beat_monitor = HeartBeatMonitor(
			heart_beat_interval,
			heart_beat_timeout,
			heart_beat_alive
			)
		GlobalData.inst.heart_beat_monitor.start()

def get_tests():
	return unittest.makeSuite(MasterServerInitializerTest)

if '__main__' == __name__:
	unittest.main()