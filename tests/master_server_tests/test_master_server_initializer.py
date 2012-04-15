import unittest
import tests.auxiliary
from master_server.master_server_initializer import MasterServerInitializer
from master_server.master_handler_register import MasterHandlerRegister

class MasterServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_initializer = MasterServerInitializer(
			'localhost:34510', 
			'localhost:34511',
			u'master_server',
			MasterHandlerRegister()
			)
		
	def test_construction(self):
		self.assertEqual(self.server_initializer.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.sub_address, 'localhost:34511')
		self.assertTrue(self.server_initializer.global_data is None)
		self.assertTrue(self.server_initializer.rmq is None)
		self.assertTrue(self.server_initializer.server_handler_dispatcher is None)
		
	def test_init_server_handler_dispatcher(self):
		self.server_initializer.init_server_handler_dispatcher()
		self.assertEqual(len(self.server_initializer.server_handler_dispatcher.handlers), 2)
		
	def test_init_global_data(self):
		self.server_initializer.init_global_data()
		self.assertEqual(len(self.server_initializer.global_data.server_manager.servers), 0)
		
	def test_init_rmq(self):
		self.server_initializer.init_global_data()
		self.server_initializer.init_rmq()
		self.assertEqual(self.server_initializer.global_data.rmq.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.global_data.rmq.sub_address, 'localhost:34511')
		self.assertEqual(self.server_initializer.global_data.rmq, self.server_initializer.rmq)
		self.assertEqual(self.server_initializer.rmq.global_data, self.server_initializer.global_data)

def get_tests():
	return unittest.makeSuite(MasterServerInitializerTest)

if '__main__' == __name__:
	unittest.main()