import unittest
import tests.auxiliary
from mock import Mock
from auth_server.create_account_handler import CreateAccountHandler
from auth_server.auth_global_data import AuthGlobalData
import auth_server.create_account_handler

class CreateAccountHandlerTest(unittest.TestCase):
	def setUp(self):
		self.create_account_handler = CreateAccountHandler()
		self.request = Mock()
		self.request.name = 'aaa'
		AuthGlobalData.inst = Mock()
		AuthGlobalData.inst.plain_class_accessor = Mock()
		AuthGlobalData.inst.redis_cluster = Mock()
		AuthGlobalData.inst.redis_cluster.get_account_redis = Mock()
		AuthGlobalData.inst.redis_cluster.get_account_redis.return_value = 1

	def test_name_exist(self):
		AuthGlobalData.inst.plain_class_accessor.setnx_user_name_to_id = Mock()
		AuthGlobalData.inst.plain_class_accessor.setnx_user_name_to_id.return_value = True

		exist = self.create_account_handler.name_exist(self.request)
		self.assertFalse(exist)
		AuthGlobalData.inst.plain_class_accessor.setnx_user_name_to_id.assert_called_with(
			1, 'aaa', 0)

	def test_create_account(self):
		self.request.password = 'bbb'
		AuthGlobalData.inst.plain_class_accessor.incr_account_id = Mock()
		AuthGlobalData.inst.plain_class_accessor.incr_account_id.return_value = 1
		AuthGlobalData.inst.plain_class_accessor.set_user_name_to_id = Mock()
		AuthGlobalData.inst.plain_class_accessor.set_user = Mock()
		user = Mock()
		auth_server.create_account_handler.User = Mock()
		auth_server.create_account_handler.User.return_value = user

		self.create_account_handler.create_account(self.request)
		self.assertTrue(AuthGlobalData.inst.redis_cluster.get_account_redis.called)
		#self.assertTrue(AuthGlobalData.inst.plain_class_accessor.incr_account_id.called)
		AuthGlobalData.inst.plain_class_accessor.incr_account_id.assert_called_with(1)
		AuthGlobalData.inst.plain_class_accessor.set_user_name_to_id.assert_called_with(
			1, 'aaa', 1)
		auth_server.create_account_handler.User.assert_called_with(1, 'aaa', 'bbb')
		AuthGlobalData.inst.plain_class_accessor.set_user.assert_called_with(1, 1, user)

def get_tests():
	return unittest.makeSuite(CreateAccountHandlerTest)

if '__main__' == __name__:
	unittest.main()