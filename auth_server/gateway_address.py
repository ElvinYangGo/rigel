import json

class GatewayAddress(object):
	def __init__(self, gateway_address_file_name):
		gateway_address_file = open(gateway_address_file_name)
		self.gateway_address_config = json.load(gateway_address_file)

	def get_wan_ip(self, server_name):
		if self.gateway_address_config.has_key(server_name):
			return self.gateway_address_config[server_name]['wan_ip']
		else:
			return None

	def get_port(self, server_name):
		if self.gateway_address_config.has_key(server_name):
			return self.gateway_address_config[server_name]['port']
		else:
			return None