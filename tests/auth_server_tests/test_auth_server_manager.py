import unittest
import tests.auxiliary
from auth_server.auth_server_manager import AuthServerManager
from common.server_type import ServerType
from common.server_status import ServerStatus

class AuthServerManagerTest(unittest.TestCase):
	def setUp(self):
		self.server_manager = AuthServerManager()
		
	def test_constructor(self):
		self.assertTrue(self.server_manager.dispatchers.has_key(ServerType.GAME_SERVER))
		self.assertTrue(self.server_manager.dispatchers.has_key(ServerType.GATEWAY_SERVER))
	
	def test_add_server(self):
		self.server_manager.add_server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		self.server_manager.add_server('sb', ServerType.GAME_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		
		self.assertEqual(len(self.server_manager.dispatchers[ServerType.GATEWAY_SERVER].servers), 1)
		self.assertEqual(len(self.server_manager.dispatchers[ServerType.GAME_SERVER].servers), 1)
		

	def test_dispatch_server(self):
		self.server_manager.add_server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		self.server_manager.add_server('sb', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		self.server_manager.add_server('sc', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
	
		self.assertEqual(self.server_manager.dispatch_server(ServerType.GATEWAY_SERVER).get_name(), 'sa')
		self.assertEqual(self.server_manager.dispatch_server(ServerType.GATEWAY_SERVER).get_name(), 'sb')
		self.assertEqual(self.server_manager.dispatch_server(ServerType.GATEWAY_SERVER).get_name(), 'sc')
		self.assertEqual(self.server_manager.dispatch_server(ServerType.GATEWAY_SERVER).get_name(), 'sa')
		
def get_tests():
	return unittest.makeSuite(AuthServerManagerTest)

if '__main__' == __name__:
	unittest.main()