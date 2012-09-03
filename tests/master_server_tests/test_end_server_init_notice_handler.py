import unittest
import tests.auxiliary
from master_server.end_server_init_notice_handler import EndServerInitNoticeHandler
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from common.server_status import ServerStatus
from common.server_type import ServerType
import protocol.server_message_pb2
from network.channel_buffer import ChannelBuffer
from mock import Mock
from protocol.server_protocol_id import ServerProtocolID

class EndServerInitNoticeHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = EndServerInitNoticeHandler()

		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = ServerManager()
		GlobalData.inst.server_manager.add_server('sa', ServerType.GATEWAY_SERVER)
		GlobalData.inst.server_manager.add_server('sb', ServerType.AUTHENTICATION_SERVER)
		GlobalData.inst.rmq = Mock()
		GlobalData.inst.rmq.send_message_string = Mock()
	
	def test_send_other_servers_to_this_server(self):
		server_list_message = GlobalData.inst.server_manager.running_server_to_net()
		self.handler.send_other_servers_to_this_server('sb')
		GlobalData.inst.rmq.send_message_string.assert_called_with(
			server_list_message, 'sb', ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)
	
	def test_send_this_server_to_other_servers(self):
		this_server_message = protocol.server_message_pb2.SyncServerNotice()
		this_server_message.servers.extend([GlobalData.inst.server_manager.get_server('sb').to_net()])
		
		self.handler.send_this_server_to_other_servers(GlobalData.inst.server_manager.get_server('sb'))
		GlobalData.inst.rmq.send_message_string.assert_called_with(
			this_server_message, 'server_status', ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)
		
	def test_handle_message(self):
		message = protocol.server_message_pb2.EndServerInitNotice()
		message.name = 'sb'
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		self.handler.handle_message(1, channel_buffer, channel_name='server_initialization')
		self.assertEqual(
			GlobalData.inst.server_manager.get_server('sb').get_status(),
			ServerStatus.SERVER_STATUS_RUNNING
			)
		
def get_tests():
	return unittest.makeSuite(EndServerInitNoticeHandlerTest)

if '__main__' == __name__:
	unittest.main()