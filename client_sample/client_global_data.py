class ClientGlobalData(object):
	channel = None
	#status: 1 connecting auth, 2 connecting gateway
	status = 0
	twisted_protocol_factory = None
	client_token = None
	server_token = None
	account_id = 0