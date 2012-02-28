import struct

class ChannelBuffer:
	def __init__(self, data=None):
		if data:
			self.buffer = data
		else:
			self.buffer = str()

	def readable_bytes(self):
		return len(self.buffer)

	def append(self, data):
		self.buffer += data

	def read_data(self, length):
		return_buffer = self.buffer[:length]
		self.buffer = self.buffer[length:]
		return return_buffer

	def read_all_data(self):
		return self.read_data(len(self.buffer))

	def get_data(self, length):
		return self.buffer[:length]

	def get_all_data(self):
		return self.buffer[:]

	def skip_data(self, length):
		self.buffer = self.buffer[length:]

	def get_int(self):
		value, = struct.unpack('!i', self.get_data(4))
		return value
		
	def read_int(self):
		value, = struct.unpack('!i', self.read_data(4))
		return value 
	
	def write_int(self, int_value):
		encoded_data = struct.pack('!i', int_value)
		self.append(encoded_data)
