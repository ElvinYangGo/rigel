class ClientConnectionInfo(object):
	def __init__(self, client_id=0, gateway_server_name='', game_server_name=''):
		self.client_id = client_id
		self.gateway_server_name = gateway_server_name
		self.game_server_name = game_server_name

	def get_client_id(self):
		return self.client_id

	def get_gateway_server_name(self):
		return self.gateway_server_name

	def get_game_server_name(self):
		return self.game_server_name