from common.global_data import GlobalData

class GatewayGlobalData(GlobalData):
	def __init__(self):
		super(GatewayGlobalData, self).__init__()
		self.server_manager = None
		self.client_rmq_pub = None
		self.channel_manager = None