import unittest
import tests.auxiliary 
from network.channel_buffer import ChannelBuffer

class ChannelBufferTest(unittest.TestCase):
	def setUp(self):
		self.channel_buffer = ChannelBuffer()

	def test_constructor(self):
		self.assertEqual(0, self.channel_buffer.readable_bytes())
		channel_buffer2 = ChannelBuffer('aaa')
		self.assertEqual(3, channel_buffer2.readable_bytes())
		
	def test_append(self):
		self.channel_buffer.append('a')
		self.assertEqual(1, self.channel_buffer.readable_bytes())
		
	def test_read_data(self):
		self.channel_buffer.append('a')
		self.assertEqual('a', self.channel_buffer.read_data(1))
		self.assertEqual(0, self.channel_buffer.readable_bytes())
		
	def test_read_all_data(self):
		self.channel_buffer.append('aaa')
		self.assertEqual('aaa', self.channel_buffer.read_all_data())
		self.assertEqual(0, self.channel_buffer.readable_bytes())
		
	def test_get_data(self):
		self.channel_buffer.append('a')
		self.assertEqual('a', self.channel_buffer.get_data(1))
		self.assertEqual(1, self.channel_buffer.readable_bytes())
		
	def test_get_all_data(self):
		self.channel_buffer.append('aaa')
		self.assertEqual('aaa', self.channel_buffer.get_all_data())
		self.assertEqual(3, self.channel_buffer.readable_bytes())
		
	def test_skip_data(self):
		self.channel_buffer.append('aaa')
		self.channel_buffer.skip_data(2)
		self.assertEqual(1, self.channel_buffer.readable_bytes())
	
	def test_write_int(self):
		self.channel_buffer.write_int(3)
		self.assertEqual(4, self.channel_buffer.readable_bytes())
	
	def test_read_int(self):
		self.channel_buffer.write_int(3)
		value = self.channel_buffer.read_int()
		self.assertEqual(3, value)
		self.assertEqual(0, self.channel_buffer.readable_bytes())
		
def get_tests():
	return unittest.makeSuite(ChannelBufferTest)

if '__main__' == __name__:
	unittest.main()

