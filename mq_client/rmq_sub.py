import zmq
import threading
from network.channel_buffer import ChannelBuffer
import common.utf8_codec

class RMQSub(threading.Thread):
	def __init__(self, sub_address, context, server_handler_dispatcher):
		self.sub_address = sub_address
		self.server_handler_dispatcher = server_handler_dispatcher

		self.sub_socket = context.socket(zmq.SUB)
		self.sub_socket.connect('tcp://' + self.sub_address)

		threading.Thread.__init__(self, name='rmq')

	def set_global_data(self, global_data):
		self.global_data = global_data

	def subscribe(self, channel_name):
		self.sub_socket.setsockopt_unicode(zmq.SUBSCRIBE, channel_name)

	def run(self):
		while True:
			message = self.sub_socket.recv()
			print message
			more = self.sub_socket.getsockopt(zmq.RCVMORE)
			if more:
				channel_name = common.utf8_codec.utf8_decode(message)
			else:
				channel_buffer = ChannelBuffer(message)
				self.server_handler_dispatcher.handle_upstream(self.global_data, channel_name, channel_buffer)
				channel_name = u''
