import unittest
import tests.auxiliary 
from mock import Mock
from network.channel import Channel

class ChannelTest(unittest.TestCase):
	def setUp(self):
		self.channel = Channel()

	def test_append_data(self):
		self.channel.append_data(bytearray('aaa'))
		self.assertEqual(3, self.channel.channel_buffer_readable_bytes())
	
	def test_set_channel_pipeline(self):
		channel_pipeline = Mock()
		self.channel.set_channel_pipeline(channel_pipeline)
		self.assertEqual(channel_pipeline, self.channel.channel_pipeline)
	
	def test_set_twisted_protocol(self):
		twisted_protocol = Mock()
		self.channel.set_twisted_protocol(twisted_protocol)
		self.assertEqual(twisted_protocol, self.channel.twisted_protocol)
	
	def test_handle_connection(self):
		channel_pipeline = Mock()
		channel_pipeline.handle_connection = Mock()
		self.channel.set_channel_pipeline(channel_pipeline)
		self.channel.handle_connection()
		channel_pipeline.handle_connection.assert_called_with()
		
	def test_handle_disconnection(self):
		channel_pipeline = Mock()
		channel_pipeline.handle_disconnection = Mock()
		self.channel.set_channel_pipeline(channel_pipeline)
		self.channel.handle_disconnection()
		channel_pipeline.handle_disconnection.assert_called_with()
	
	def test_handle_upstream(self):
		channel_pipeline = Mock()
		channel_pipeline.handle_upstream = Mock()
		self.channel.set_channel_pipeline(channel_pipeline)
		self.channel.handle_upstream()
		channel_pipeline.handle_upstream.assert_called_with(self.channel.channel_buffer)
		
	def test_send(self):
		channel_pipeline = Mock()
		channel_pipeline.handle_downstream = Mock()
		channel_buffer = Mock()
		self.channel.set_channel_pipeline(channel_pipeline)
		self.channel.send(channel_buffer)
		channel_pipeline.handle_downstream.assert_called_with(channel_buffer)
		
	def test_write_to_twisted_protocol(self):
		twisted_protocol = Mock()
		twisted_protocol.transport = Mock()
		twisted_protocol.transport.write = Mock()
		data = Mock()
		self.channel.set_twisted_protocol(twisted_protocol)
		self.channel.write_to_twisted_protocol(data)
		twisted_protocol.transport.write.assert_called_with(data)
	
	def test_get_remote_ip(self):
		twisted_protocol = Mock()
		twisted_protocol.get_remote_ip = Mock()
		twisted_protocol.get_remote_ip.return_value = "192.168.0.1"
		self.channel.set_twisted_protocol(twisted_protocol)
		self.assertEqual("192.168.0.1", self.channel.get_remote_ip())
		
	
	def test_get_remote_port(self):
		twisted_protocol = Mock()
		twisted_protocol.get_remote_port = Mock()
		twisted_protocol.get_remote_port.return_value = 111
		self.channel.set_twisted_protocol(twisted_protocol)
		self.assertEqual(111, self.channel.get_remote_port())
	
def get_tests():
	return unittest.makeSuite(ChannelTest)

if '__main__' == __name__:
	unittest.main()

