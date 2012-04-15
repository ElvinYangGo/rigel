import unittest
import tests.auxiliary
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID
from master_server.master_handler_register import MasterHandlerRegister

class MasterHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = MasterHandlerRegister()
		server_handler_dispatcher = handler_register.register(ServerHandlerDispatcher())
		self.assertEqual(len(server_handler_dispatcher.handlers), 2)
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.START_SERVER_INIT_REQUEST))
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.END_SERVER_INIT_NOTIFICATION))

def get_tests():
	return unittest.makeSuite(MasterHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()