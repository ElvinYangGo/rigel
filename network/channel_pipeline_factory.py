import copy
from network.channel_pipeline import ChannelPipeline

class ChannelPipelineFactory:
	def __init__(self):
		self.handlers = []
		
	def append_handler(self, name, handler):
		self.handlers.append((name, handler))
	
	def create_pipeline(self):
		return ChannelPipeline(copy.deepcopy(self.handlers))
		