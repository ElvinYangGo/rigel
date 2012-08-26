import unittest
import tests.auxiliary
from common.handler_dispatcher import HandlerDispatcher
from protocol.server_protocol_id import ServerProtocolID
from auth_server.auth_handler_register import AuthHandlerRegister

class AuthHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = AuthHandlerRegister()
		handler_dispatcher = handler_register.register(HandlerDispatcher())
		self.assertEqual(len(handler_dispatcher.handlers), 2)
		self.assertTrue(handler_dispatcher.handlers.has_key(ServerProtocolID.P_START_SERVER_INIT_RES))
		self.assertTrue(handler_dispatcher.handlers.has_key(ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE))

def get_tests():
	return unittest.makeSuite(AuthHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()