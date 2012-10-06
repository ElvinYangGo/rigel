from common.global_data import GlobalData

class AuthGlobalData(GlobalData):
	def __init__(self):
		super(AuthGlobalData, self).__init__()
		self.server_manager = None
		self.gateway_address = None