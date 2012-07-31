from twisted.internet.protocol import Factory
from network.channel_factory import ChannelFactory 
from network.twisted_protocol import TwistedProtocol

class TwistedProtocolFactory(Factory):
	def __init__(self, channel_pipeline_factory, channel_manager):
		self.channel_factory = ChannelFactory(channel_pipeline_factory, channel_manager)
	
	def buildProtocol(self, addr):
		return TwistedProtocol(self.channel_factory.create_channel())

	def startFactory(self):
		pass
	
	def stopFactory(self):
		pass
