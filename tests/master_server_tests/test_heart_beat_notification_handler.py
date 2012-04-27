import unittest
import tests.auxiliary
from master_server.heart_beat_notification_handler import HeartBeatNotificationHandler
import protocol
from network.channel_buffer import ChannelBuffer
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from common.server_type import ServerType
from common.server_status import ServerStatus

class HeartBeatNotificationHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = HeartBeatNotificationHandler()
	
	def test_handle_message(self):
		message = protocol.protocol_message_pb2.HeartBeatNotification()
		message.name = u'sa'
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		global_data.server_manager.add_server('sa', ServerType.AUTHENTICATION_SERVER)
		global_data.server_manager.get_server('sa').set_status(ServerStatus.SERVER_STATUS_CLOSED)
		
		self.handler.handle_message(global_data, 'test_channel', 1, channel_buffer)
		self.assertTrue(global_data.server_manager.get_server('sa').get_heart_beat_time() != 0)
		self.assertEqual(global_data.server_manager.get_server('sa').get_status(), ServerStatus.SERVER_STATUS_RUNNING)
		
def get_tests():
	return unittest.makeSuite(HeartBeatNotificationHandlerTest)

if '__main__' == __name__:
	unittest.main()