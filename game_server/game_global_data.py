from common.global_data import GlobalData

class GameGlobalData(GlobalData):
	def __init__(self):
		super(GameGlobalData, self).__init__()
		self.server_manager = None
		self.server_name = None