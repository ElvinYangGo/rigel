from network.channel import Channel

class ChannelFactory:
	def __init__(self, channel_pipeline_factory):
		self.channel_pipeline_factory = channel_pipeline_factory
	
	def create_channel(self):
		channel_pipeline = self.channel_pipeline_factory.create_channel_pipeline()
		channel = Channel()
		channel_pipeline.set_channel(channel)
		channel.set_channel_pipeline(channel_pipeline)
		return channel