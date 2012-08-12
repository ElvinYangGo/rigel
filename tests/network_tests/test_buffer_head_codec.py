import unittest
import tests.auxiliary
import struct
from mock import Mock
from network.buffer_head_codec import BufferHeadCodec
from network.channel_buffer import ChannelBuffer

class BufferHeadCodecTest(unittest.TestCase):
	def setUp(self):
		self.buffer_head_codec = BufferHeadCodec()
		self.channel_buffer = ChannelBuffer()
	
	def test_handle_upstream(self):
		return_value = self.buffer_head_codec.handle_upstream(self.channel_buffer)
		self.assertEqual(None, return_value)
		
		raw_buffer = '123'
		encoded_data = struct.pack('!i' + str(len(raw_buffer)) + 's', len(raw_buffer), raw_buffer)
		self.channel_buffer.append(encoded_data)
		return_value = self.buffer_head_codec.handle_upstream(self.channel_buffer)
		self.assertEqual(raw_buffer, return_value.get_all_data())
		
	def test_handle_downstream(self):
		raw_buffer = '123'
		self.channel_buffer.append(raw_buffer)
		return_value = self.buffer_head_codec.handle_downstream(self.channel_buffer)
		encoded_data = struct.pack('!i' + str(len(raw_buffer)) + 's', len(raw_buffer), raw_buffer)
		self.assertEqual(encoded_data, return_value.get_all_data())

def get_tests():
	return unittest.makeSuite(BufferHeadCodecTest)

if '__main__' == __name__:
	unittest.main()