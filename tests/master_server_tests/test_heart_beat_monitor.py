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
from common.channel_name import ChannelName
from protocol.server_protocol_id import ServerProtocolID

class HeartBeatMonitorTest(unittest.TestCase):
	def setUp(self):
		self.current_time = time.time()
		self.server = Server('aaa', ServerType.GAME_SERVER)
		self.server.set_heart_beat_time(self.current_time)
		self.heart_beat_monitor = HeartBeatMonitor(10000, 60000, 15000)
		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = ServerManager()

	def test_server_timeout(self):
		self.assertFalse(self.heart_beat_monitor.server_timeout(self.current_time, self.server))
		self.assertTrue(self.heart_beat_monitor.server_timeout(self.current_time+61, self.server))

	def test_server_alive(self):
		self.assertTrue(self.heart_beat_monitor.server_alive(self.current_time, self.server))
		self.assertFalse(self.heart_beat_monitor.server_alive(self.current_time+16, self.server))

	def test_broadcast_server_status(self):
		GlobalData.inst.server_manager.to_net = Mock()
		GlobalData.inst.server_manager.to_net.return_value = Mock()
		GlobalData.inst.rmq = Mock()
		GlobalData.inst.rmq.send_message = Mock()

		self.heart_beat_monitor.broadcast_server_status()

		self.assertTrue(GlobalData.inst.server_manager.to_net.called)
		GlobalData.inst.rmq.send_message.assert_called_with(
			GlobalData.inst.server_manager.to_net.return_value,
			ChannelName.SERVER_STATUS,
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)

	def test_change_server_status(self):
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

		self.heart_beat_monitor.change_server_status()

		self.assertEqual(server_a.get_status(), ServerStatus.SERVER_STATUS_CLOSED)
		self.assertEqual(server_b.get_status(), ServerStatus.SERVER_STATUS_RUNNING)

def get_tests():
	return unittest.makeSuite(HeartBeatMonitorTest)

if '__main__' == __name__:
	unittest.main()