import json

class MQConfig(object):
	def __init__(self, config_file_name=None, config_string=None):
		if config_file_name:
			with open(config_file_name) as f:
				self.config = json.load(f)
		else:
			self.config = json.loads(config_string)

	def get_pub_address(self):
		return self.config['pub_address']
	
	def get_sub_address(self):
		return self.config['sub_address']