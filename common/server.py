class Server(object):
	def __init__(self, name, type, status):
		self.name = name
		self.type = type
		self.status = status
		
	def get_name(self):
		return self.name
	
	def get_type(self):
		return self.type
	
	def get_status(self):
		return self.status
	