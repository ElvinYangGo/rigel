import unittest
import tests.auxiliary
from mock import Mock
from auth_server.login_auth_handler import LoginAuthHandler
from auth_server.auth_global_data import AuthGlobalData
import auth_server.login_auth_handler
from protocol.client_protocol_id import ClientProtocolID

class LoginAuthHandlerTest(unittest.TestCase):
	def setUp(self):
		self.login_auth_handler = LoginAuthHandler()
		self.channel = Mock()
		self.response = Mock()
		self.request = Mock()
		auth_server.login_auth_handler.send_result = Mock()
		AuthGlobalData.inst = Mock()
		AuthGlobalData.inst.plain_class_accessor = Mock()
		
	def test_valid_user_name(self):
		AuthGlobalData.inst.plain_class_accessor.get_user_name_to_id = Mock()
	
		AuthGlobalData.inst.plain_class_accessor.get_user_name_to_id.return_value = 1 
		ok, account_id = self.login_auth_handler.valid_user_name(self.channel, self.request, self.response)
		self.assertTrue(ok)
		self.assertEqual(account_id, 1)
		self.assertFalse(auth_server.login_auth_handler.send_result.called)

		AuthGlobalData.inst.plain_class_accessor.get_user_name_to_id.return_value = 0 
		ok, account_id = self.login_auth_handler.valid_user_name(self.channel, self.request, self.response)
		self.assertFalse(ok)
		self.assertEqual(account_id, 0)
		auth_server.login_auth_handler.send_result.assert_called_with(
			self.channel, 
			self.response,
			ClientProtocolID.P_LOGIN_AUTH_RES, 
			ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_NOT_EXIST
			)
		
	def test_valid_user_name_and_password(self):
		user = Mock()
		user.get_user_name = Mock()
		user.get_password = Mock()
		user.get_user_name.return_value = u'aaa'
		user.get_password.return_value = u'aaa'
		AuthGlobalData.inst.plain_class_accessor.get_user.return_value = user
		self.request.name = u'aaa'
		self.request.password = u'aaa'
		ok = self.login_auth_handler.valid_user_name_and_password(self.channel, self.request, self.response, 1)
		self.assertTrue(ok)
	
		self.request.password = u'bbb'
		ok = self.login_auth_handler.valid_user_name_and_password(self.channel, self.request, self.response, 1)
		self.assertFalse(ok)
		auth_server.login_auth_handler.send_result.assert_called_with(
			self.channel, 
			self.response,
			ClientProtocolID.P_LOGIN_AUTH_RES, 
			ClientProtocolID.R_LOGIN_AUTH_RES_USER_NAME_OR_PASSWORD_INVALID
			)
		
	def test_save_client_connection_info_to_redis(self):
		client_connection_info = Mock()
		auth_server.login_auth_handler.ClientConnectionInfo = Mock()
		auth_server.login_auth_handler.ClientConnectionInfo.return_value = client_connection_info
		AuthGlobalData.inst.redis_cluster.get_redis = Mock()
		r = Mock()
		AuthGlobalData.inst.redis_cluster.get_redis.return_value = r
		AuthGlobalData.inst.plain_class_accessor.set_client_connection_info = Mock()
		AuthGlobalData.inst.plain_class_accessor.expire_client_connection_info = Mock()
		self.login_auth_handler.save_client_connection_info_to_redis(3, 'aaa', Mock(), Mock())
		AuthGlobalData.inst.plain_class_accessor.set_client_connection_info.assert_called_with(
			r, 3, client_connection_info)
		AuthGlobalData.inst.plain_class_accessor.expire_client_connection_info.assert_called_with(
			r, 3, 10)
		
	def test_fill_success_response(self):
		gateway_server = Mock()
		AuthGlobalData.inst.gateway_address.get_wan_ip = Mock()
		AuthGlobalData.inst.gateway_address.get_wan_ip.return_value = '111'
		AuthGlobalData.inst.gateway_address.get_port = Mock()
		AuthGlobalData.inst.gateway_address.get_port.return_value = 222
		res = self.login_auth_handler.fill_success_response(self.response, 3, 'aaa', gateway_server)
		self.assertEqual(res.server_token, 'aaa')
		self.assertEqual(res.gateway_ip, '111')
		self.assertEqual(res.gateway_port, 222)
		self.assertEqual(res.account_id, 3)
		
def get_tests():
	return unittest.makeSuite(LoginAuthHandlerTest)

if '__main__' == __name__:
	unittest.main()