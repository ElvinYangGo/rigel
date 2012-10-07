import unittest
import tests.auxiliary
from common.server import Server
from common.server_type import ServerType
from common.server_status import ServerStatus

class ServerTest(unittest.TestCase):
	def setUp(self):
		self.server = Server('aaa', ServerType.AUTH_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		
	def test_construction(self):
		self.assertEqual(self.server.get_name(), 'aaa')
		self.assertEqual(self.server.get_type(), ServerType.AUTH_SERVER)
		self.assertEqual(self.server.get_status(), ServerStatus.SERVER_STATUS_RUNNING)
		self.assertFalse(self.server.closed())
		self.assertFalse(self.server.starting())
		self.assertTrue(self.server.running())

	def test_compare_status(self):
		self.assertTrue(self.server.compare_status(ServerStatus.SERVER_STATUS_RUNNING))
		self.assertFalse(self.server.compare_status(ServerStatus.SERVER_STATUS_CLOSED))

def get_tests():
	return unittest.makeSuite(ServerTest)

if '__main__' == __name__:
	unittest.main()