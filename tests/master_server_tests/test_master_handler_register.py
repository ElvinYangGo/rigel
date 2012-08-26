import unittest
import tests.auxiliary
from common.handler_dispatcher import HandlerDispatcher
from protocol.server_protocol_id import ServerProtocolID
from master_server.master_handler_register import MasterHandlerRegister

class MasterHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = MasterHandlerRegister()
		handler_dispatcher = handler_register.register(HandlerDispatcher())
		self.assertEqual(len(handler_dispatcher.handlers), 3)
		self.assertTrue(handler_dispatcher.handlers.has_key(ServerProtocolID.P_START_SERVER_INIT_REQ))
		self.assertTrue(handler_dispatcher.handlers.has_key(ServerProtocolID.P_END_SERVER_INIT_NOTICE))

def get_tests():
	return unittest.makeSuite(MasterHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()