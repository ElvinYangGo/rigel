from common.global_data import GlobalData

class GatewayGlobalData(GlobalData):
	server_manager = None
	server_name = None
	rmq_pub = None
	channel_manager = None