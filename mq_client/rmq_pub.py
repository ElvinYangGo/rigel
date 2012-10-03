import zmq
from network.channel_buffer import ChannelBuffer

class RMQPub(object):
	def __init__(self, pub_address, context, pipeline):
		self.pub_address = pub_address
		self.pipeline = pipeline
		self.pub_socket = context.socket(zmq.PUB)
		self.pub_socket.connect('tcp://' + self.pub_address)

	def send_message(self, message, channel_name=u'', message_id=0, **kwargs):
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message.SerializeToString())
		self.send_channel_buffer(channel_buffer, channel_name, message_id, **kwargs)

	def send_channel_buffer(self, channel_buffer, channel_name=u'', message_id=0, **kwargs):
		if channel_buffer is None and message_id == 0:
			return

		buffer_after_pipeline = self.pipeline.handle_downstream(channel_buffer, **kwargs)

		self.pub_socket.send_unicode(channel_name, zmq.SNDMORE)
		buffer_to_send = None
		if message_id != 0:
			buffer_to_send = ChannelBuffer()
			buffer_to_send.write_int(message_id)
			if buffer_after_pipeline is not None:
				buffer_to_send.append(buffer_after_pipeline.get_all_data())
		else:
			buffer_to_send = buffer_after_pipeline

		self.pub_socket.send(buffer_to_send.read_all_data())
