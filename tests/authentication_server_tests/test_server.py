import unittest
import tests.auxiliary
from common.server import Server
from common.server_type import ServerType
from common.server_status import ServerStatus

class ServerTest(unittest.TestCase):
	def setUp(self):
		self.server = Server('aaa', ServerType.AUTHENTICATION_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		
	def test_construction(self):
		self.assertEqual(self.server.get_name(), 'aaa')
		self.assertEqual(self.server.get_type(), ServerType.AUTHENTICATION_SERVER)
		self.assertEqual(self.server.get_status(), ServerStatus.SERVER_STATUS_RUNNING)

def get_tests():
	return unittest.makeSuite(ServerTest)

if '__main__' == __name__:
	unittest.main()