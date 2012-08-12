from common.global_data import GlobalData

class CenterGlobalData(GlobalData):
	def __init__(self):
		super(CenterGlobalData, self).__init__()
		self.server_manager = None
		self.server_name = None