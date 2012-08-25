import unittest
import tests.auxiliary
from authentication_server.auth_server_manager import AuthServerManager
from common.server import Server
from common.server_type import ServerType
from common.server_status import ServerStatus

class AuthServerManagerTest(unittest.TestCase):
	def setUp(self):
		self.server_manager = AuthServerManager()
		
	def test_constructor(self):
		self.assertEqual(self.server_manager.game_server_index, 0)
		self.assertEqual(len(self.server_manager.game_servers), 0)
		self.assertEqual(self.server_manager.gateway_server_index, 0)
		self.assertEqual(len(self.server_manager.gateway_servers), 0)
		
	def test_add_server(self):
		self.server_manager.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_manager.add_server(Server('sb', ServerType.GAME_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		
		self.assertEqual(len(self.server_manager.gateway_servers), 1)
		self.assertEqual(len(self.server_manager.game_servers), 1)
		
	def test_dispatch_gateway_server(self):
		self.server_manager.add_server(Server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_manager.add_server(Server('sb', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_manager.add_server(Server('sc', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
	
		self.assertEqual(self.server_manager.dispatch_gateway_server().get_name(), 'sa')
		self.assertEqual(self.server_manager.dispatch_gateway_server().get_name(), 'sb')
		self.assertEqual(self.server_manager.dispatch_gateway_server().get_name(), 'sc')
		self.assertEqual(self.server_manager.dispatch_gateway_server().get_name(), 'sa')
		
	def test_dispatch_game_server(self):
		self.server_manager.add_server(Server('sd', ServerType.GAME_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_manager.add_server(Server('se', ServerType.GAME_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		self.server_manager.add_server(Server('sf', ServerType.GAME_SERVER, ServerStatus.SERVER_STATUS_RUNNING))
		
		self.assertEqual(self.server_manager.dispatch_game_server().get_name(), 'sd')
		self.assertEqual(self.server_manager.dispatch_game_server().get_name(), 'se')
		self.assertEqual(self.server_manager.dispatch_game_server().get_name(), 'sf')
		self.assertEqual(self.server_manager.dispatch_game_server().get_name(), 'sd')
		self.assertEqual(self.server_manager.dispatch_game_server().get_name(), 'se')

def get_tests():
	return unittest.makeSuite(AuthServerManagerTest)

if '__main__' == __name__:
	unittest.main()