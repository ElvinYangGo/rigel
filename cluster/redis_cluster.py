from cluster.redis_server import RedisServer
from cluster.redis_partition import RedisPartition

class RedisCluster(object):
	def __init__(self, server_file_name, partition_file_name):
		self.redis_server = RedisServer(server_file_name)
		self.redis_partition = RedisPartition(partition_file_name)

	def get_redis(self, id):
		name = self.redis_partition.get_server_name(id)
		return self.redis_server.get_redis(name)

	def get_account_redis(self):
		return self.redis_server.get_redis('account')

	def get_center_redis(self):
		return self.redis_server.get_redis("center")
