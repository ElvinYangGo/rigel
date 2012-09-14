import unittest
import tests.auxiliary
from auth_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler
import protocol.server_message_pb2
import protocol.server_data_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from common.global_data import GlobalData
from auth_server.auth_server_manager import AuthServerManager
from common.server import Server
from mock import Mock

class SyncServerStatusNoticeHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = SyncServerStatusNoticeHandler()
		
	def test_handle_running_server(self):
		server_net = protocol.server_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.AUTHENTICATION_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = protocol.server_data_pb2.Server()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_RUNNING
		
		GlobalData.inst = Mock()
		GlobalData.inst.server_manager = AuthServerManager()
		
		self.handler.handle_running_server(server_net)
		self.handler.handle_running_server(server_net2)
		
		self.assertEqual(len(GlobalData.inst.server_manager.dispatchers[ServerType.GATEWAY_SERVER].servers), 1)
		self.assertTrue(GlobalData.inst.server_manager.contain_server(ServerType.GATEWAY_SERVER, 'sb'))
		self.assertEqual(GlobalData.inst.server_manager.dispatchers[ServerType.GATEWAY_SERVER].servers[0].get_type(), ServerType.GATEWAY_SERVER)
		self.assertEqual(GlobalData.inst.server_manager.dispatchers[ServerType.GATEWAY_SERVER].servers[0].get_status(), ServerStatus.SERVER_STATUS_RUNNING)

	def test_handle_closed_server(self):
		server = Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		GlobalData.inst = Mock()
		GlobalData.inst.server_manager = AuthServerManager()
		GlobalData.inst.server_manager.add_server(server)
		
		server_net = protocol.server_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_CLOSED
	
		self.handler.handle_closed_server(server_net)
		
		self.assertEqual(len(GlobalData.inst.server_manager.dispatchers[ServerType.GATEWAY_SERVER].servers), 0)
		
	def test_handle_message(self):
		message = protocol.server_message_pb2.SyncServerNotice()
		server_net = message.servers.add()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = message.servers.add()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_CLOSED
		
		channel_buffer = ChannelBuffer(message.SerializeToString())
		self.handler.handle_closed_server = Mock()
		self.handler.handle_running_server = Mock()
		
		self.handler.handle_message(1, channel_buffer, channel_name='test_channel')
		
		self.handler.handle_running_server.assert_called_with(server_net)
		self.handler.handle_closed_server.assert_called_with(server_net2)

def get_tests():
	return unittest.makeSuite(SyncServerStatusNoticeHandlerTest)

if '__main__' == __name__:
	unittest.main()