import unittest
import tests.auxiliary
from master_server.server import Server
from common.server_status import ServerStatus
from common.server_type import ServerType
import protocol.protocol_pb2

class ServerTest(unittest.TestCase):
	def setUp(self):
		self.server = Server('aaa', ServerType.AUTHENTICATION_SERVER)
	
	def test_construction(self):
		self.assertTrue(self.server.starting())
		self.assertEqual(self.server.get_type(), ServerType.AUTHENTICATION_SERVER)
		
	def test_set_status(self):
		self.server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
		self.assertTrue(self.server.running())
		
		self.server.set_status(ServerStatus.SERVER_STATUS_CLOSED)
		self.assertTrue(self.server.closed())
		self.assertFalse(self.server.starting())
		self.assertFalse(self.server.running())
	
	def test_to_net_string(self):
		net_string = self.server.to_net_string()
		message = protocol.protocol_pb2.Server.FromString(net_string)
		self.assertEqual(message.name, self.server.get_name())
		self.assertEqual(message.status, self.server.status)

def get_tests():
	return unittest.makeSuite(ServerTest)

if '__main__' == __name__:
	unittest.main()