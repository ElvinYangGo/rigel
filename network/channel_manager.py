class ChannelManager(object):
	def __init__(self):
		self.channels = {}

	def insert(self, id, channel):
		self.channels[id] = channel

	def remove(self, id):
		del self.channels[id]

	def get_channel(self, id):
		return self.channels[id]