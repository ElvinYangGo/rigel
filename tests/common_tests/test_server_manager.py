import unittest
import tests.auxiliary
from mock import Mock
from common.server_manager import ServerManager
from common.server_status import ServerStatus

class ServerManagerTest(unittest.TestCase):
	def setUp(self):
		self.server_manager = ServerManager()
		
	def test_add_server(self):
		self.assertEqual(len(self.server_manager.servers), 0)
		self.server_manager.add_server('sa', 1, 1)
		self.assertEqual(len(self.server_manager.servers), 1)

	def test_server_running(self):
		self.server_manager.add_server('sa', 1, ServerStatus.SERVER_STATUS_RUNNING)
		self.server_manager.add_server('sb', 1, ServerStatus.SERVER_STATUS_CLOSED)

		self.assertTrue(self.server_manager.server_running('sa'))
		self.assertFalse(self.server_manager.server_running('sb'))
		self.assertFalse(self.server_manager.server_running('sc'))

def get_tests():
	return unittest.makeSuite(ServerManagerTest)

if '__main__' == __name__:
	unittest.main()