import zmq
import threading
from network.channel_buffer import ChannelBuffer

class RMQ(threading.Thread):
	def __init__(self, pub_address, sub_address, server_handler_dispatcher):
		self.pub_address = 'tcp://' + pub_address
		self.sub_address = 'tcp://' + sub_address
		self.server_handler_dispatcher = server_handler_dispatcher
		
		context = zmq.Context()
		self.pub_socket = context.socket(zmq.PUB)
		self.pub_socket.connect(pub_address)
		self.sub_socket = context.socket(zmq.SUB)
		self.sub_socket.connect(sub_address)
		
		threading.Thread.__init__(self, name='rmq')
		
	def set_global_data(self, global_data):
		self.global_data = global_data
		
	def subscribe(self, channel_name):
		self.sub_socket.setsockopt(zmq.SUBSCRIBE, channel_name)
	
	def run(self):
		while True:
			message = self.sub_socket.recv()
			print message
			more = self.sub_socket.getsockopt(zmq.RCVMORE)
			if more:
				channel_name = message
			else:
				channel_buffer = ChannelBuffer(message)
				self.server_handler_dispatcher.handle_upstream(self.global_data, channel_name, channel_buffer)
				channel_name = ''
				
	def send(self, channel_buffer, channel_name='', message_id=0):
		if channel_buffer is None and message_id == 0:
			return
		
		self.pub_socket.send(channel_name, zmq.SNDMORE)
		buffer_to_send = None
		if message_id != 0:
			buffer_to_send = ChannelBuffer()
			buffer_to_send.write_int(message_id)
			if channel_buffer is not None:
				buffer_to_send.append(channel_buffer.get_all_data())
		else:
			buffer_to_send = channel_buffer
			
		self.pub_socket.send(buffer_to_send.read_all_data())
