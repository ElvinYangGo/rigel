import unittest
import tests.auxiliary
from mock import Mock
from master_server.heart_beat_monitor import HeartBeatMonitor
from master_server.server import Server
from common.server_type import ServerType
import time
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from common.server_status import ServerStatus
import master_server.heart_beat_monitor

class HeartBeatMonitorTest(unittest.TestCase):
	def setUp(self):
		self.current_time = time.time()
		self.server = Server('aaa', ServerType.GAME_SERVER)
		self.server.set_heart_beat_time(self.current_time)
		self.heart_beat_monitor = HeartBeatMonitor(10000, 60000, 15000)

	def test_server_timeout(self):
		self.assertFalse(self.heart_beat_monitor.server_timeout(self.current_time, self.server))
		self.assertTrue(self.heart_beat_monitor.server_timeout(self.current_time+61, self.server))

	def test_server_alive(self):
		self.assertTrue(self.heart_beat_monitor.server_alive(self.current_time, self.server))
		self.assertFalse(self.heart_beat_monitor.server_alive(self.current_time+16, self.server))

	def test_broadcast_server_status(self):
		server2 = Server('bbb', ServerType.GAME_SERVER)
		changed_server_list = []
		changed_server_list.append(self.server)
		changed_server_list.append(server2)
		GlobalData.inst = Mock()
		self.heart_beat_monitor.broadcast_server_status(changed_server_list)

	def test_get_changed_server_list(self):
		GlobalData.inst.server_manager = ServerManager()
		GlobalData.inst.server_manager.add_server('aaa', ServerType.GAME_SERVER)
		GlobalData.inst.server_manager.add_server('bbb', ServerType.GAME_SERVER)
		GlobalData.inst.server_manager.add_server('ccc', ServerType.GAME_SERVER)
		server_a = GlobalData.inst.server_manager.get_server('aaa')
		server_a.set_status(ServerStatus.SERVER_STATUS_RUNNING)
		server_a.set_heart_beat_time(10)
		server_b = GlobalData.inst.server_manager.get_server('bbb')
		server_b.set_status(ServerStatus.SERVER_STATUS_CLOSED)
		server_b.set_heart_beat_time(90)
		master_server.heart_beat_monitor.time = Mock()
		master_server.heart_beat_monitor.time.time = Mock()
		master_server.heart_beat_monitor.time.time.return_value = 100 
		changed_server_list = self.heart_beat_monitor.get_changed_server_list()
		self.assertEqual(len(changed_server_list), 2)

	def get_changed_server_list(self):
		changed_server_list = []
		current_time = time.time()
		for server in GlobalData.inst.server_manager.get_all_servers().itervalues():
			if server.running() and self.server_timeout(current_time, server):
				server.set_status(ServerStatus.SERVER_STATUS_CLOSED)
				changed_server_list.append(server)
			if server.closed() and self.server_alive(current_time, server):
				server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
				changed_server_list.append(server)
		return changed_server_list

def get_tests():
	return unittest.makeSuite(HeartBeatMonitorTest)

if '__main__' == __name__:
	unittest.main()