import zmq
from network.channel_buffer import ChannelBuffer

class RMQPub(object):
	def __init__(self, pub_address, context):
		self.pub_address = pub_address
		self.pub_socket = context.socket(zmq.PUB)
		self.pub_socket.connect('tcp://' + self.pub_address)

	def set_global_data(self, global_data):
		self.global_data = global_data

	def send_message_string(self, message_string, channel_name=u'', message_id=0):
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message_string.SerializeToString())
		self.send_channel_buffer(channel_buffer, channel_name, message_id)

	def send_channel_buffer(self, channel_buffer, channel_name=u'', message_id=0):
		if channel_buffer is None and message_id == 0:
			return

		self.pub_socket.send_unicode(channel_name, zmq.SNDMORE)
		buffer_to_send = None
		if message_id != 0:
			buffer_to_send = ChannelBuffer()
			buffer_to_send.write_int(message_id)
			if channel_buffer is not None:
				buffer_to_send.append(channel_buffer.get_all_data())
		else:
			buffer_to_send = channel_buffer

		self.pub_socket.send(buffer_to_send.read_all_data())
