import unittest
import tests.auxiliary
from mock import Mock
from network.channel_pipeline_factory import ChannelPipelineFactory

class ChannelPipelineFactoryTest(unittest.TestCase):
	def setUp(self):
		self.channel_pipeline_factory = ChannelPipelineFactory()
	
	def test_create_channel_pipeline_factory(self):
		handler = Mock()
		self.channel_pipeline_factory.append_handler('test', handler)
		channel_pipeline = self.channel_pipeline_factory.create_pipeline()
		self.assertEqual(1, channel_pipeline.handler_count())
		self.assertTrue(handler is not channel_pipeline.handlers[0][1])

def get_tests():
	return unittest.makeSuite(ChannelPipelineFactoryTest)

if '__main__' == __name__:
	unittest.main()