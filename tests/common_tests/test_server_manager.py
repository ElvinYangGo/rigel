import unittest
import tests.auxiliary
from mock import Mock
from common.server_manager import ServerManager

class ServerManagerTest(unittest.TestCase):
	def setUp(self):
		self.server_manager = ServerManager()
		
	def test_add_server(self):
		self.assertEqual(len(self.server_manager.servers), 0)
		self.server_manager.add_server('sa', 1, 1)
		self.assertEqual(len(self.server_manager.servers), 1)

def get_tests():
	return unittest.makeSuite(ServerManagerTest)

if '__main__' == __name__:
	unittest.main()