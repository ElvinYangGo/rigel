import unittest
import tests.auxiliary
from mock import Mock
from game_server.create_avatar_handler import CreateAvatarHandler
from game_server.game_global_data import GameGlobalData
import protocol.client_message_pb2
from protocol.client_protocol_id import ClientProtocolID
from protocol.server_protocol_id import ServerProtocolID

class CreateAvatarHandlerTest(unittest.TestCase):
	def setUp(self):
		self.create_avatar_handler = CreateAvatarHandler()
		self.client_conn_info = Mock()
		self.client_conn_info.client_id = 1

	def test_create_avatar(self):
		request = Mock()
		request.name = 'a'
		request.gender = 1
		request.level = 2
		GameGlobalData.inst = Mock()
		self.create_avatar_handler.create_avatar(self.client_conn_info, request)

	def test_handle_message(self):
		self.client_conn_info.gateway_server_name = 'aaa'
		self.create_avatar_handler.create_avatar = Mock()
		GameGlobalData.inst = Mock()
		GameGlobalData.inst.rmq = Mock()
		GameGlobalData.inst.rmq.send_message = Mock()
		response = protocol.client_message_pb2.CreateAvatarRes()
		response.result = ClientProtocolID.R_CREATE_AVATAR_RES_SUCCESS
		GameGlobalData.inst.rmq.send_message.assert_calles_with(
			response,
			'aaa',
			ServerProtocolID.P_SERVER_TO_CLIENT_RELAY,
			1,
			ClientProtocolID.P_CREATE_AVATAR_RES
			)

def get_tests():
	return unittest.makeSuite(CreateAvatarHandlerTest)

if '__main__' == __name__:
	unittest.main()