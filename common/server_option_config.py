class ServerOptionConfig:
	def __init__(self, heart_beat_interval, heart_beat_timeout):
		self.heart_beat_interval = heart_beat_interval
		self.heart_beat_timeout = heart_beat_timeout
		
	def get_heart_beat_interval(self):
		return self.heart_beat_interval
	
	def get_heart_beat_timeout(self):
		return self.heart_beat_timeout