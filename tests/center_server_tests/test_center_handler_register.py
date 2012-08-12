import unittest
import tests.auxiliary
from common.handler_dispatcher import HandlerDispatcher
from protocol.protocol_id import ProtocolID
from center_server.center_handler_dispatcher import CenterHandlerRegister

class CenterHandlerRegisterTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_register(self):
		handler_register = CenterHandlerRegister()
		handler_dispatcher = handler_register.register(HandlerDispatcher())
		self.assertEqual(len(handler_dispatcher.handlers), 2)
		self.assertTrue(handler_dispatcher.handlers.has_key(ProtocolID.START_SERVER_INIT_RESPONSE))
		self.assertTrue(handler_dispatcher.handlers.has_key(ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION))

def get_tests():
	return unittest.makeSuite(CenterHandlerRegisterTest)

if '__main__' == __name__:
	unittest.main()