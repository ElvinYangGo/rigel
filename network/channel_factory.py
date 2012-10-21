from network.channel import Channel

class ChannelFactory(object):
	def __init__(self, channel_pipeline_factory, channel_manager):
		self.channel_pipeline_factory = channel_pipeline_factory
		self.channel_manager = channel_manager
	
	def create_channel(self):
		channel_pipeline = self.channel_pipeline_factory.create_pipeline()
		channel = Channel()
		channel_pipeline.set_channel(channel)
		channel.set_channel_pipeline(channel_pipeline)
		channel.set_channel_manager(self.channel_manager)
		return channel