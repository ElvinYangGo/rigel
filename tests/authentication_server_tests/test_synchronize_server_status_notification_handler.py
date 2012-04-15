import unittest
import tests.auxiliary
from authentication_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler
import protocol.protocol_message_pb2
import protocol.protocol_data_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from authentication_server.global_data import GlobalData
from common.server_manager import ServerManager
from common.server import Server
from mock import Mock

class SynchronizeServerStatusNotificationHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = SynchronizeServerStatusNotificationHandler()
		
	def test_handle_running_server(self):
		server_net = protocol.protocol_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.AUTHENTICATION_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = protocol.protocol_data_pb2.Server()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_RUNNING
		
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		
		self.handler.handle_running_server(global_data, server_net)
		self.handler.handle_running_server(global_data, server_net2)
		
		self.assertEqual(len(global_data.server_manager.servers), 1)
		self.assertEqual(global_data.server_manager.servers.get('sb').get_name(), 'sb')
		self.assertEqual(global_data.server_manager.servers.get('sb').get_type(), ServerType.GATEWAY_SERVER)
		self.assertEqual(global_data.server_manager.servers.get('sb').get_status(), ServerStatus.SERVER_STATUS_RUNNING)

	def test_handle_closed_server(self):
		server = Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		global_data = GlobalData()
		global_data.server_manager = ServerManager()
		global_data.server_manager.add_server(server)
		
		server_net = protocol.protocol_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
	
		self.handler.handle_closed_server(global_data, server_net)
		
		self.assertEqual(len(global_data.server_manager.servers), 0)
		
	def test_handle_message(self):
		message = protocol.protocol_message_pb2.SynchronizeServerNotification()
		server_net = message.servers.add()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = message.servers.add()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_CLOSED
		
		channel_buffer = ChannelBuffer(message.SerializeToString())
		global_data = GlobalData()
		self.handler.handle_closed_server = Mock()
		self.handler.handle_running_server = Mock()
		
		self.handler.handle_message(global_data, 'test_channel', 1, channel_buffer)
		
		self.handler.handle_running_server.assert_called_with(global_data, server_net)
		self.handler.handle_closed_server.assert_called_with(global_data, server_net2)

def get_tests():
	return unittest.makeSuite(SynchronizeServerStatusNotificationHandlerTest)

if '__main__' == __name__:
	unittest.main()