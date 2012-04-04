import zmq
from mq_client.rmq import RMQ
from common.server_handler_dispatcher import ServerHandlerDispatcher
from master_server.start_server_init_request_handler import StartServerInitRequestHandler 
from master_server.end_server_init_notification_handler import EndServerInitNotificationHandler
from protocol.protocol_id import ProtocolID
from master_server.global_data import GlobalData
from master_server.server_manager import ServerManager

if __name__ == '__main__':
	print 'master started'
	
	global_data = GlobalData()
	global_data.server_manager = ServerManager()
	
	server_handler_dispatcher = ServerHandlerDispatcher()
	server_handler_dispatcher.append_handler(
		ProtocolID.START_SERVER_INIT_REQUEST, 
		StartServerInitRequestHandler()
		)
	server_handler_dispatcher.append_handler(
		ProtocolID.END_SERVER_INIT_NOTIFICATION, 
		EndServerInitNotificationHandler()
		)

	rmq = RMQ('tcp://localhost:34510', 'tcp://localhost:34511', server_handler_dispatcher)
	rmq.subscribe('server_initialization')
	rmq.subscribe('server_status')
	#rmq.subscribe('')
	
	global_data.rmq = rmq	
	rmq.set_global_data(global_data)
	rmq.start()
