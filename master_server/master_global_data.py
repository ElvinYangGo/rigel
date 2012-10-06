from common.global_data import GlobalData

class MasterGlobalData(GlobalData):
	def __init__(self):
		super(MasterGlobalData, self).__init__()
		self.server_manager = None
		self.heart_beat_monitor = None