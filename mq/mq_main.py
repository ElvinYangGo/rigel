import zmq

if __name__ == '__main__':
	print 'started'
	
	context = zmq.Context()
	
	frontend = context.socket(zmq.SUB)
	frontend.bind('tcp://*:34510')
	
	backend = context.socket(zmq.PUB)
	backend.bind('tcp://*:34511')
	
	frontend.setsockopt(zmq.SUBSCRIBE, '')

	while True:
		message = frontend.recv()
		more = frontend.getsocket(zmq.RCVMORE)
		if more:
			backend.send(message, zmq.SNDMORE)
		else:
			backend.send(message)