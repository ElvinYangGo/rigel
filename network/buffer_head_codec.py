import struct
from network.channel_buffer import ChannelBuffer

class BufferHeadCodec(object):
	HEAD_LENGTH = struct.calcsize('!H')

	def handle_upstream(self, channel_buffer, **kwargs):
		if BufferHeadCodec.HEAD_LENGTH < channel_buffer.readable_bytes():
			packet_length, = struct.unpack('!H', channel_buffer.get_data(BufferHeadCodec.HEAD_LENGTH))
			if BufferHeadCodec.HEAD_LENGTH + packet_length <= channel_buffer.readable_bytes():
				channel_buffer.skip_data(BufferHeadCodec.HEAD_LENGTH)
				return ChannelBuffer(channel_buffer.read_data(packet_length))
		return None

	def handle_downstream(self, channel_buffer, **kwargs):
		raw_buffer = channel_buffer.get_all_data()
		encoded_data = struct.pack('!H' + str(len(raw_buffer)) + 's', len(raw_buffer), raw_buffer)
		return ChannelBuffer(encoded_data)

