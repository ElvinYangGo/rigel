import struct
from network.channel_buffer import ChannelBuffer

class BufferHeadCodec:
	MESSAGE_ID_LENGTH = struct.calcsize('!i')

	def handle_upstream(self, channel, channel_buffer):
		if BufferHeadCodec.MESSAGE_ID_LENGTH < channel_buffer.readable_bytes():
			packet_length, = struct.unpack('!i', channel_buffer.get_data(BufferHeadCodec.MESSAGE_ID_LENGTH))
			if BufferHeadCodec.MESSAGE_ID_LENGTH + packet_length <= channel_buffer.readable_bytes():
				channel_buffer.skip_data(BufferHeadCodec.MESSAGE_ID_LENGTH)
				return ChannelBuffer(channel_buffer.read_data(packet_length))
		return None

	def handle_downstream(self, channel, channel_buffer):
		raw_buffer = channel_buffer.get_all_data()
		encoded_data = struct.pack('!i' + str(len(raw_buffer)) + 's', len(raw_buffer), raw_buffer)
		return ChannelBuffer(encoded_data)

