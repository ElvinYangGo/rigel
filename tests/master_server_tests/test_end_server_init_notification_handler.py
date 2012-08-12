import unittest
import tests.auxiliary
from master_server.end_server_init_notification_handler import EndServerInitNotificationHandler
from common.global_data import GlobalData
from master_server.server_manager import ServerManager
from common.server_status import ServerStatus
from common.server_type import ServerType
import protocol.protocol_message_pb2
from network.channel_buffer import ChannelBuffer
from mock import Mock
from protocol.protocol_id import ProtocolID

class EndServerInitNotificationHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = EndServerInitNotificationHandler()

		GlobalData.instance = GlobalData()
		GlobalData.instance.server_manager = ServerManager()
		GlobalData.instance.server_manager.add_server('sa', ServerType.GATEWAY_SERVER)
		GlobalData.instance.server_manager.add_server('sb', ServerType.AUTHENTICATION_SERVER)
		GlobalData.instance.rmq = Mock()
		GlobalData.instance.rmq.send_message_string = Mock()
	
	def test_send_other_servers_to_this_server(self):
		server_list_message = GlobalData.instance.server_manager.running_server_to_net()
		self.handler.send_other_servers_to_this_server('sb')
		GlobalData.instance.rmq.send_message_string.assert_called_with(server_list_message, 'sb', ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)
	
	def test_send_this_server_to_other_servers(self):
		this_server_message = protocol.protocol_message_pb2.SynchronizeServerNotification()
		this_server_message.servers.extend([GlobalData.instance.server_manager.get_server('sb').to_net()])
		
		self.handler.send_this_server_to_other_servers(GlobalData.instance.server_manager.get_server('sb'))
		GlobalData.instance.rmq.send_message_string.assert_called_with(this_server_message, 'server_status', ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)
		
	def test_handle_message(self):
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = 'sb'
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		self.handler.handle_message(1, channel_buffer, channel_name='server_initialization')
		self.assertEqual(GlobalData.instance.server_manager.get_server('sb').get_status(), ServerStatus.SERVER_STATUS_RUNNING)
		
def get_tests():
	return unittest.makeSuite(EndServerInitNotificationHandlerTest)

if '__main__' == __name__:
	unittest.main()