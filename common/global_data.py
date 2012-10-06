class GlobalData(object):
	inst = None

	def __init__(self):
		self.zmq_context = None
		self.rmq = None
		self.heart_beat_rmq_pub = None
		self.redis_cluster = None
		self.plain_class_accessor = None
		self.server_option_config = None
		self.server_name = None
		self.server_status = None