import unittest
import tests.auxiliary
from mock import Mock
from common.server_initializer import ServerInitializer
from common.global_data import GlobalData

class ServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.handler_register = Mock()
		self.handler_register.register = Mock()
		self.server_initializer = ServerInitializer(
			'localhost:34510',
			'localhost:34511', 
			u'authentication_server',
			self.handler_register
			)
		
	def test_construction(self):
		self.assertEqual(self.server_initializer.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.sub_address, 'localhost:34511')
		self.assertTrue(self.server_initializer.global_data is None)
		self.assertTrue(self.server_initializer.rmq is None)
		self.assertTrue(self.server_initializer.server_handler_dispatcher is None)
		
	def test_init_server_handler_dispatcher(self):
		self.server_initializer.init_server_handler_dispatcher()
		self.assertTrue(self.handler_register.register.called)
		
	def test_init_rmq(self):
		self.server_initializer.global_data = GlobalData()
		self.server_initializer.global_data.server_name = u'game_server'
		self.server_initializer.init_rmq()
		self.assertEqual(self.server_initializer.global_data.rmq.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.global_data.rmq.sub_address, 'localhost:34511')
		self.assertEqual(self.server_initializer.global_data.rmq, self.server_initializer.rmq)
		self.assertEqual(self.server_initializer.rmq.global_data, self.server_initializer.global_data)

def get_tests():
	return unittest.makeSuite(ServerInitializerTest)

if '__main__' == __name__:
	unittest.main()