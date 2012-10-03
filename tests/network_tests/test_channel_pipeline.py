import unittest
import tests.auxiliary 
from mock import Mock
from network.channel_pipeline import ChannelPipeline
from network.channel import Channel

class ChannelPipelineTest(unittest.TestCase):
	def setUp(self):
		self.channel_pipeline = ChannelPipeline()
		
	def test_constructor(self):
		handlers = []
		handlers.append(('test', Mock()))
		channel_pipeline_init = ChannelPipeline(handlers)
		self.assertEqual(1, channel_pipeline_init.handler_count())
		
	def test_append_handler(self):
		handler = Mock()
		self.channel_pipeline.append_handler('test', handler)
		self.assertEqual(1, self.channel_pipeline.handler_count())
	
	def test_remove_handler(self):
		handler = Mock()
		self.channel_pipeline.append_handler('test', handler)
		self.channel_pipeline.remove_handler('test')
		self.assertEqual(0, self.channel_pipeline.handler_count())
	
	def test_handle_connection(self):
		handler_a = Mock()
		def fun_a(channel):
			channel.v += 2
		handler_a.handle_connection = fun_a
		
		handler_b = Mock()
		def fun_b(channel):
			channel.v *= 3
		handler_b.handle_connection = fun_b
		
		channel = Mock()
		channel.v = 1
		self.channel_pipeline.set_channel(channel)
		self.channel_pipeline.append_handler('handler_a', handler_a)
		self.channel_pipeline.append_handler('handler_b', handler_b)
		self.channel_pipeline.handle_connection()
		self.assertEqual(5, channel.v)
		
	def test_handle_disconnection(self):
		handler_a = Mock()
		def fun_a(channel):
			channel.v += 2
		handler_a.handle_disconnection = fun_a
		
		handler_b = Mock()
		def fun_b(channel):
			channel.v *= 3
		handler_b.handle_disconnection = fun_b
		
		channel = Mock()
		channel.v = 1
		self.channel_pipeline.set_channel(channel)
		self.channel_pipeline.append_handler('handler_a', handler_a)
		self.channel_pipeline.append_handler('handler_b', handler_b)
		self.channel_pipeline.handle_disconnection()
		self.assertEqual(5, channel.v)
		
	def test_handle_upstream(self):
		handler_a = Mock()
		def fun_a(channel_buffer, **kwargs):
			channel_buffer.v *= 4
			return channel_buffer
		handler_a.handle_upstream = fun_a
		
		handler_b = Mock()
		def fun_b(channel_buffer, **kwargs):
			return None
		handler_b.handle_upstream = fun_b
		
		handler_c = Mock()
		def fun_c(channel_buffer, **kwargs):
			channel_buffer.v *= 3
			return channel_buffer
		handler_c.handle_upstream = fun_c
		
		channel_buffer = Mock()
		channel_buffer.v = 1
		self.channel_pipeline.set_channel(Mock())
		self.channel_pipeline.append_handler('handler_a', handler_a)
		self.channel_pipeline.append_handler('handler_b', handler_b)
		self.channel_pipeline.append_handler('handler_c', handler_c)
		self.channel_pipeline.handle_upstream(channel_buffer)
		self.assertEqual(3, channel_buffer.v)
	
	def test_handle_downstream(self):
		handler_a = Mock()
		def fun_a(channel_buffer, **kwargs):
			channel_buffer.v *= 4
			return channel_buffer
		handler_a.handle_downstream = fun_a
		
		handler_b = Mock()
		def fun_b(channel_buffer, **kwargs):
			return channel_buffer
		handler_b.handle_downstream = fun_b
		
		handler_c = Mock()
		def fun_c(channel_buffer, **kwargs):
			channel_buffer.v *= 3
			return channel_buffer
		handler_c.handle_downstream = fun_c
		
		channel_buffer = Mock()
		channel_buffer.v = 1
		def fun_read_all_data(): 
			return 3
		channel_buffer.read_all_data = fun_read_all_data
		
		channel = Channel()
		channel.write_to_twisted_protocol = Mock()
		self.channel_pipeline.set_channel(channel)
		self.channel_pipeline.append_handler('handler_a', handler_a)
		self.channel_pipeline.append_handler('handler_b', handler_b)
		self.channel_pipeline.append_handler('handler_c', handler_c)
		buff = self.channel_pipeline.handle_downstream(channel_buffer)
		#channel.write_to_twisted_protocol.assert_called_with(3)
		self.assertEqual(12, buff.v)
		
def get_tests():
	return unittest.makeSuite(ChannelPipelineTest)

if '__main__' == __name__:
	unittest.main()

