import unittest
import tests.auxiliary
from mock import Mock
from common.server_type import ServerType
from auth_server.server_dispatcher import ServerDispatcher
from common.server import Server
from common.server_status import ServerStatus

class ServerDispatcherTest(unittest.TestCase):
	def setUp(self):
		self.server_dispatcher = ServerDispatcher(ServerType.GATEWAY_SERVER)

	def test_contain_server(self):
		self.assertFalse(self.server_dispatcher.contain_server('sa'))
		self.server_dispatcher.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.assertTrue(self.server_dispatcher.contain_server('sa'))
		
	def test_add_server(self):
		self.server_dispatcher.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.assertEqual(len(self.server_dispatcher.servers), 1)
		
	def test_remove_server(self):
		self.server_dispatcher.remove_server('sa')
		self.server_dispatcher.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_dispatcher.remove_server('sa')
		self.assertEqual(len(self.server_dispatcher.servers), 0)

	def test_dispatch_server(self):
		self.server_dispatcher.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_dispatcher.add_server(Server('sb', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_dispatcher.add_server(Server('sc', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))

		self.assertEqual(self.server_dispatcher.dispatch_server().get_name(), 'sa')
		self.assertEqual(self.server_dispatcher.dispatch_server().get_name(), 'sb')
		self.assertEqual(self.server_dispatcher.dispatch_server().get_name(), 'sc')
		self.assertEqual(self.server_dispatcher.dispatch_server().get_name(), 'sa')

def get_tests():
	return unittest.makeSuite(ServerDispatcherTest)

if '__main__' == __name__:
	unittest.main()