import unittest
import tests.auxiliary
from common.server_handler_dispatcher import ServerHandlerDispatcher
from protocol.protocol_id import ProtocolID
from authentication_server.authentication_handler_register import AuthenticationHandlerRegister

class AuthenticationHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = AuthenticationHandlerRegister()
		server_handler_dispatcher = handler_register.register(ServerHandlerDispatcher())
		self.assertEqual(len(server_handler_dispatcher.handlers), 2)
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.START_SERVER_INIT_RESPONSE))
		self.assertTrue(server_handler_dispatcher.handlers.has_key(ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION))

def get_tests():
	return unittest.makeSuite(AuthenticationHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()