import unittest
import tests.auxiliary
from mock import Mock
from gateway_server.login_gateway_handler import LoginGatewayHandler
from gateway_server.gateway_global_data import GatewayGlobalData
from protocol.client_protocol_id import ClientProtocolID

class LoginGatewayHandlerTest(unittest.TestCase):
	def setUp(self):
		self.login_gateway_handler = LoginGatewayHandler()
	"""
		r = GatewayGlobalData.inst.redis_cluster.get_redis(request.account_id)
		client_connection_info = GatewayGlobalData.inst.plain_class_accessor.get_client_connection_info(
			r,
			request.account_id
			)
		if client_connection_info is None:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED

		if client_connection_info.get_token() != request.token:
			return False, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_INVALID

		return True"""
	def test_valid_token(self):
		GatewayGlobalData.inst = Mock()
		GatewayGlobalData.inst.redis_cluster = Mock()
		GatewayGlobalData.inst.redis_cluster.get_redis = Mock()
		GatewayGlobalData.inst.redis_cluster.get_redis.return_value = 1
		GatewayGlobalData.inst.plain_class_accessor = Mock()
		request = Mock()
		request.account_id = 11
		request.token = 'aaa'

		valid, error = self.login_gateway_handler.valid_token(request, None)
		self.assertFalse(valid)
		self.assertEqual(error, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED)

		client_connection_info = Mock()
		client_connection_info.get_token = Mock()
		client_connection_info.get_token.return_value = 'bbb'

		valid, error = self.login_gateway_handler.valid_token(request, client_connection_info)
		self.assertFalse(valid)
		self.assertEqual(error, ClientProtocolID.R_LOGIN_GATEWAY_RES_TOKEN_INVALID)

		client_connection_info.get_token.return_value = 'aaa'

		valid, error = self.login_gateway_handler.valid_token(request, client_connection_info)
		self.assertTrue(valid)
		self.assertEqual(error, None)

def get_tests():
	return unittest.makeSuite(LoginGatewayHandlerTest)

if '__main__' == __name__:
	unittest.main()