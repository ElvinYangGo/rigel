from common.global_data import GlobalData

class AuthenticationGlobalData(GlobalData):
	def __init__(self):
		super(AuthenticationGlobalData, self).__init__()
		self.server_manager = None
		self.server_name = None
		self.channel_manager = None