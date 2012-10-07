import unittest
import tests.auxiliary
from master_server.init_server_req_handler import InitServerReqHandler
import protocol.server_message_pb2
from common.server_type import ServerType
from network.channel_buffer import ChannelBuffer
from mock import Mock
from common.global_data import GlobalData
from master_server.master_server_manager import MasterServerManager
from protocol.server_protocol_id import ServerProtocolID
from common.channel_name import ChannelName
from common.server_status import ServerStatus

class InitServerReqHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = InitServerReqHandler()

		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = MasterServerManager()
		GlobalData.inst.server_manager.add_server('sa', ServerType.GATEWAY_SERVER)
		GlobalData.inst.server_manager.add_server('sb', ServerType.AUTH_SERVER)
		GlobalData.inst.rmq = Mock()
		GlobalData.inst.rmq.send_message_string = Mock()
		GlobalData.inst.rmq.send_channel_buffer = Mock()

	def test_send_other_servers_to_this_server(self):
		server_list_message = GlobalData.inst.server_manager.to_net()
		self.handler.send_other_servers_to_this_server('sb')
		GlobalData.inst.rmq.send_message.assert_called_with(
			server_list_message, 'sb', ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)

	def test_send_this_server_to_other_servers(self):
		this_server_message = protocol.server_message_pb2.SyncServerNotice()
		this_server_message.servers.extend([GlobalData.inst.server_manager.get_server('sb').to_net()])

		self.handler.send_this_server_to_other_servers(GlobalData.inst.server_manager.get_server('sb'))
		GlobalData.inst.rmq.send_message.assert_called_with(
			this_server_message, 'server_status', ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)

	def test_handle_message(self):
		message = protocol.server_message_pb2.InitServerReq()
		message.name = 'sc'
		message.type = ServerType.AUTH_SERVER
		channel_buffer = ChannelBuffer(message.SerializeToString())
		self.handler.send_other_servers_to_this_server = Mock()
		self.handler.send_this_server_to_other_servers = Mock()

		self.handler.handle_message(1, channel_buffer, channel_name=ChannelName.SERVER_INIT)

		self.assertNotEqual(GlobalData.inst.server_manager.get_server('sc'), None)
		server = GlobalData.inst.server_manager.get_server('sc')
		self.assertEqual(server.get_status(), ServerStatus.SERVER_STATUS_RUNNING)
		self.assertNotEqual(server.get_heart_beat_time(), 0)
		GlobalData.inst.rmq.send_channel_buffer.assert_called_with(
			None, 'sc', ServerProtocolID.P_INIT_SERVER_RES
			)
		self.handler.send_other_servers_to_this_server.assert_called_with('sc')
		self.assertTrue(self.handler.send_this_server_to_other_servers.called)

def get_tests():
	return unittest.makeSuite(InitServerReqHandlerTest)

if '__main__' == __name__:
	unittest.main()