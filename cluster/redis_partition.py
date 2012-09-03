import json

class RedisPartition(object):
	def __init__(self, file_name):
		self.init_partitions(file_name)

	def init_partitions(self, file_name):
		with open(file_name) as f:
			self.partitions = json.load(f)

	def get_server_name(self, id):
		for partition in self.partitions:
			if partition['start'] <= id and id <= partition['end']:
				return partition['server']
		return None