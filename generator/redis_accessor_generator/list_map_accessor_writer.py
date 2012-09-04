from generator.redis_accessor_generator.list_map_list_accessor_writer import ListMapListAccessorWriter
from generator.redis_accessor_generator.list_map_map_accessor_writer import ListMapMapAccessorWriter

class ListMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f

	def write(self):
		list_map_list_accessor_writer = ListMapListAccessorWriter(self.table_desc, self.f)
		list_map_list_accessor_writer.write()
		list_map_map_accessor_writer = ListMapMapAccessorWriter(self.table_desc, self.f)
		list_map_map_accessor_writer.write()

"""
	def get_friend_list(self, redis, id_string):
		return redis.lrange(self.redis_key.get_friend_list_key(id_string), 0, -1)

	def get_friend_dict_list(self, redis, id_string):
		friend_string_list = self.get_friend_list(redis, id_string)
		friend_dict_list = []
		with redis.pipeline() as pipe:
			for friend_string in friend_string_list:
				pipe.hgetall(self.redis_key.get_friend_key(id_string, friend_string))
			friend_dict_list = pipe.execute()
		return friend_dict_list

	def add_friend(self, redis, id_string, friend_string, d):
		redis.rpush(self.redis_key.get_friend_list_key(id_string), friend_string)
		redis.hmset(self.redis_key.get_friend_key(id_string, friend_string), d)

	def remove_friend(self, redis, id_string, friend_string):
		redis.lrem(self.redis_key.get_friend_list_key(id_string), 0, friend_string)
		redis.del(self.redis_key.get_friend_key(id_string, friend_string))

	def get_friend(self, redis, id_string, friend_string):
		return redis.hgetall(self.redis_key.get_friend_key(id_string, friend_string))

	def set_friend(self, redis, id_string, friend_string, d):
		redis.hmset(self.redis_key.get_friend_key(id_string, friend_string), d)

	def get_friend_table_user_name(self, redis, id_string, friend_string):
		return redis.hget(
			self.redis_key.get_friend_key(id_string, friend_string),
			self.redis_key.get_friend_table_user_name_field()
			)

	def set_friend_table_user_name(self, redis, id_string, friend_string, user_name_string):
		redis.hset(
			self.redis_key.get_friend_key(id_string, friend_string),
			self.redis_key.get_friend_table_user_name_field(),
			user_name_string
			)

	def get_friend_table_user_id(self, redis, id_string, friend_string):
		return redis.hget(
			self.redis_key.get_friend_key(id_string, friend_string),
			self.redis_key.get_friend_table_user_id_field()
			)

	def set_friend_table_user_id(self, redis, id_string, friend_string, user_id_string):
		redis.hset(
			self.redis_key.get_friend_key(id_string, friend_string),
			self.redis_key.get_friend_table_user_id_field(),
			user_id_string
			)

"""