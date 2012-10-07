import unittest
import tests.auxiliary
from mock import Mock
from gateway_server.login_gateway_handler import LoginGatewayHandler
from gateway_server.gateway_global_data import GatewayGlobalData
from protocol.client_protocol_id import ClientProtocolID
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2

class LoginGatewayHandlerTest(unittest.TestCase):
	def setUp(self):
		self.login_gateway_handler = LoginGatewayHandler()

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

	def test_send_prepare_avatar_notice(self):
		GatewayGlobalData.inst = Mock()
		GatewayGlobalData.inst.client_rmq_pub = Mock()
		GatewayGlobalData.inst.client_rmq_pub.send_message = Mock()
		prepare_avatar_notice = protocol.server_message_pb2.PrepareAvatarNotice()
		prepare_avatar_notice.account_id = 1

		self.login_gateway_handler.send_prepare_avatar_notice(1, 'sa')
		GatewayGlobalData.inst.client_rmq_pub.send_message.assert_called_with(
			prepare_avatar_notice,
			'sa',
			ServerProtocolID.P_PREPARE_AVATAR_NOTICE
			)
	def send_prepare_avatar_notice(self, account_id, game_server_name):
		prepare_avatar_notice = protocol.server_message_pb2.PrepareAvatarNotice()
		prepare_avatar_notice.account_id = account_id
		GatewayGlobalData.inst.client_rmq_pub.send_message(
			prepare_avatar_notice,
			game_server_name,
			ServerProtocolID.P_PREPARE_AVATAR_NOTICE
			)
def get_tests():
	return unittest.makeSuite(LoginGatewayHandlerTest)

if '__main__' == __name__:
	unittest.main()