import unittest
import tests.auxiliary
from master_server.handler_register import HandlerRegister
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID

class HandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = HandlerRegister()
		server_handler_dispatcher = handler_register.register(ServerHandlerDispatcher())
		self.assertEqual(len(server_handler_dispatcher.handlers), 2)
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.START_SERVER_INIT_REQUEST))
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.END_SERVER_INIT_NOTIFICATION))

def get_tests():
	return unittest.makeSuite(HandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()