import json

class ServerOptionConfig(object):
	def __init__(self, config_file_name=None, config_string=None):
		if config_file_name:
			with open(config_file_name) as f:
				self.config = json.load(f)
		else:
			self.config = json.loads(config_string)

	def get_heart_beat_interval(self):
		return self.config['heart_beat_interval']
	
	def get_heart_beat_timeout(self):
		return self.config['heart_beat_timeout']

	def get_heart_beat_alive(self):
		return self.config['heart_beat_alive']

	def to_json_string(self):
		return json.dumps(self.config)