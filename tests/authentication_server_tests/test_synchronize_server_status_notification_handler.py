import unittest
import tests.auxiliary
from authentication_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler
from authentication_server.global_data import GlobalData
from authentication_server.server_manager import ServerManager
import protocol.protocol_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from protocol.protocol_id import ProtocolID

class SynchronizeServerStatusNotificationHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = SynchronizeServerStatusNotificationHandler()
		
	def test_handle_message(self):
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		
		message_encoded = protocol.protocol_pb2.SynchronizeServerNotification()
		server_encoded = message_encoded.servers.add()
		server_encoded.name = 'aaa'
		server_encoded.type = ServerType.AUTHENTICATION_SERVER
		server_encoded.status = ServerStatus.SERVER_STATUS_RUNNING
		
		channel_buffer = ChannelBuffer(data=message_encoded.SerializeToString())
		
		self.handler.handle_message(
								global_data, 
								'server_status', 
								ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION, 
								channel_buffer
								)
		
		self.assertEqual(len(global_data.server_manager.servers), 1)
		server = global_data.server_manager.servers.get('aaa')
		self.assertEqual(server.get_name(), 'aaa')
		self.assertEqual(server.get_type(), ServerType.AUTHENTICATION_SERVER)
		self.assertEqual(server.get_status(), ServerStatus.SERVER_STATUS_RUNNING)

def get_tests():
	return unittest.makeSuite(SynchronizeServerStatusNotificationHandlerTest)

if '__main__' == __name__:
	unittest.main()