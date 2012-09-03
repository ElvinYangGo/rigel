import json
import redis

class RedisServer(object):
	def __init__(self, file_name):
		self.servers = {} #{name:redis}
		self.init_servers(file_name)

	def init_servers(self, file_name):
		with open(file_name) as f:
			server_config_list = json.load(f)
			for server_config in server_config_list:
				r = redis.StrictRedis(
					host=server_config['host'],
					port=server_config['port']
					)
				self.servers[server_config['name']] = r

	def get_redis(self, name):
		return self.servers.get(name)