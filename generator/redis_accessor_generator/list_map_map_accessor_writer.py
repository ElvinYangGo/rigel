from generator.redis_accessor_generator.map_accessor_writer import MapAccessorWriter

class ListMapMapAccessorWriter(MapAccessorWriter):
	def __init__(self, table_desc, f):
		super(ListMapMapAccessorWriter, self).__init__(table_desc, f)
		
	def get_key_param_string(self):
		return 'id_string, {}_string'.format(self.table_desc['table_name'])

"""

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