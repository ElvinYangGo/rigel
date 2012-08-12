class GlobalData(object):
	instance = None

	def __init__(self):
		self.zmq_context = None
		self.rmq = None
