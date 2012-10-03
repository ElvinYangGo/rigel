import unittest
import tests.auxiliary
from mock import Mock
from gateway_server.client_message_relay import ClientMessageRelay

class ClientMessageRelayTest(unittest.TestCase):
	def setUp(self):
		self.client_message_relay = ClientMessageRelay()
	
	def test_get_channel_name(self):
		channel = Mock()
		protocol_id = 0x0201
		name = self.client_message_relay.get_channel_name(channel, protocol_id)
		self.assertEqual(name, 'center_server')
		
		channel.get_game_server_name = Mock()
		channel.get_game_server_name.return_value = 'game_server'
		protocol_id = 0x1001
		name = self.client_message_relay.get_channel_name(channel, protocol_id)
		self.assertEqual(name, 'game_server')
		
def get_tests():
	return unittest.makeSuite(ClientMessageRelayTest)

if '__main__' == __name__:
	unittest.main()