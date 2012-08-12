import unittest
import tests.auxiliary
from common.handler_dispatcher import HandlerDispatcher
from protocol.protocol_id import ProtocolID
from master_server.master_handler_register import MasterHandlerRegister

class MasterHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = MasterHandlerRegister()
		handler_dispatcher = handler_register.register(HandlerDispatcher())
		self.assertEqual(len(handler_dispatcher.handlers), 3)
		self.assertTrue(handler_dispatcher.handlers.has_key(ProtocolID.START_SERVER_INIT_REQUEST))
		self.assertTrue(handler_dispatcher.handlers.has_key(ProtocolID.END_SERVER_INIT_NOTIFICATION))

def get_tests():
	return unittest.makeSuite(MasterHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()