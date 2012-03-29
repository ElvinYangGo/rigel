import zmq

if __name__ == '__main__':
	print 'started'
	
	context = zmq.Context()
	
	sub_socket = context.socket(zmq.SUB)
	sub_socket.bind('tcp://*:34510')
	
	pub_socket = context.socket(zmq.PUB)
	pub_socket.bind('tcp://*:34511')
	
	sub_socket.setsockopt(zmq.SUBSCRIBE, '')

	while True:
		message = sub_socket.recv()
		more = sub_socket.getsockopt(zmq.RCVMORE)
		if more:
			pub_socket.send(message, zmq.SNDMORE)
		else:
			pub_socket.send(message)