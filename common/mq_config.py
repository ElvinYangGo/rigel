class MQConfig:
	def __init__(self, pub_address, sub_address):
		self.pub_address = pub_address
		self.sub_address = sub_address
		
	def get_pub_address(self):
		return self.pub_address
	
	def get_sub_address(self):
		return self.sub_address