import zmq
from mq_client.rmq import RMQ
from common.server_handler_dispatcher import ServerHandlerDispatcher
from master_server.start_server_init_request_handler import StartServerInitRequestHandler 
from protocol.protocol_id import ProtocolID
from master_server.global_data import GlobalData
from master_server.server_manager import ServerManager

if __name__ == '__main__':
	print 'master started'
	
	"""
	context = zmq.Context()
	
	pub_socket = context.socket(zmq.PUB)
	pub_socket.connect('tcp://localhost:34510')
	
	sub_socket = context.socket(zmq.SUB)
	sub_socket.connect('tcp://localhost:34511')
	
	sub_socket.setsockopt(zmq.SUBSCRIBE, 'server_initialization')

	while True:
		message = sub_socket.recv()
		print message
		more = sub_socket.getsockopt(zmq.RCVMORE)
		if more:
			pass
		else:
			sub_socket.setsockopt(zmq.SUBSCRIBE, message)
			
			pub_socket.send(message, zmq.SNDMORE)
			pub_socket.send('aaa')
	"""		
		
	global_data = GlobalData()
	global_data.server_manager = ServerManager()
	
	server_handler_dispatcher = ServerHandlerDispatcher()
	server_handler_dispatcher.append_handler(
		ProtocolID.START_SERVER_INIT_REQUEST, 
		StartServerInitRequestHandler()
		)
	rmq = RMQ('tcp://localhost:34510', 'tcp://localhost:34511', server_handler_dispatcher)
	rmq.subscribe('server_initialization')
	#rmq.subscribe('')
	
	global_data.rmq = rmq	
	rmq.set_global_data(global_data)
	rmq.start()
