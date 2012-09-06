from generator.redis_accessor_generator.map_accessor_writer import MapAccessorWriter
from generator.redis_accessor_generator.list_accessor_writer import ListAccessorWriter
from generator.redis_accessor_generator.list_map_accessor_writer import ListMapAccessorWriter
from generator.redis_accessor_generator.global_list_accessor_writer import GlobalListAccessorWriter
from generator.redis_accessor_generator.global_sorted_set_accessor_writer import GlobalSortedSetAccessorWriter
from generator.redis_accessor_generator.sorted_set_accessor_writer import SortedSetAccessorWriter
from generator.redis_accessor_generator.pair_map_accessor_writer import PairMapAccessorWriter

class RedisAccessorWriter(object):
	def __init__(self, file_name, table_desc_array):
		self.file_name = file_name
		self.table_desc_array = table_desc_array

	def write(self):
		with open(self.file_name, 'w') as f:
			self.write_class_head(f)
			self.write_class_body(f)
			f.flush()
	
	def write_class_head(self, f):
		f.write('#This file is generated by program. DO NOT EDIT IT MANUALLY!\n')
		f.write('from redis_client.redis_key import RedisKey\n\n')
		f.write('class RedisAccessor(object):\n')
		f.write('\tdef __init__(self):\n')
		f.write('\t\tself.redis_key = RedisKey()\n\n')
	
	def write_class_body(self, f):
		self.write_pexpire_function(f)
		self.write_expire_function(f)

		for table_desc in self.table_desc_array:
			table_type = table_desc['table_type']
			if table_type == 'map':
				map_accessor_writer = MapAccessorWriter(table_desc, f)
				map_accessor_writer.write()
			elif table_type == 'list':
				list_accessor_writer = ListAccessorWriter(table_desc, f)
				list_accessor_writer.write()
			elif table_type == 'list_map':
				list_map_accessor_writer = ListMapAccessorWriter(table_desc, f)
				list_map_accessor_writer.write()
			elif table_type == 'global_list':
				global_list_accessor_writer = GlobalListAccessorWriter(table_desc, f)
				global_list_accessor_writer.write()
			elif table_type == 'global_sorted_set':
				global_sorted_set_accessor_writer = GlobalSortedSetAccessorWriter(table_desc, f)
				global_sorted_set_accessor_writer.write()
			elif table_type == 'sorted_set':
				sorted_set_accessor_writer = SortedSetAccessorWriter(table_desc, f)
				sorted_set_accessor_writer.write()
			elif table_type == 'pair_map':
				pair_map_accessor_writer = PairMapAccessorWriter(table_desc, f)
				pair_map_accessor_writer.write()

	def write_pexpire_function(self, f):
		f.write('\tdef pexpire(self, redis, key, milliseconds):\n')
		f.write('\t\tredis.pexpire(key, milliseconds)\n\n')
		
	def write_expire_function(self, f):
		f.write('\tdef expire(self, redis, key, seconds):\n')
		f.write('\t\tredis.expire(key, seconds)\n\n')

"""
from redis_client.redis_table import RedisTable

class RedisAccessor(object):
	def __init__(self):
		self.redis_table = RedisTable()

	def get_user(self, redis, id_string):
		return redis.hgetall(self.redis_table.get_user_key(id_string))

	def set_user(self, redis, id_string, d):
		redis.hmset(self.redis_table.get_user_key(id_string), d)

	def get_user_table_user_name(self, redis, id_string):
		return redis.hget(
			self.redis_table.get_user_key(id_string),
			self.redis_table.get_user_table_user_name_field()
			)

	def set_user_table_user_name(self, redis, id_string, user_name_string):
		redis.hset(
			self.redis_table.get_user_key(id_string),
			self.redis_table.get_user_table_user_name_field(),
			user_name_string
			)

	def get_user_table_user_id(self, redis, id_string):
		return redis.hget(
			self.redis_table.get_user_key(id_string),
			self.redis_table.get_user_table_user_id_field()
			)

	def set_user_table_user_id(self, redis, id_string, user_id_string):
		redis.hset(
			self.redis_table.get_user_key(id_string),
			self.redis_table.get_user_table_user_id_field(),
			user_id_string
			)

	def get_item_list(self, redis, id_string):
		return redis.lrange(self.redis_table.get_item_list_key(id_string), 0, -1)

	def add_item(self, redis, id_string, item_string):
		redis.rpush(self.redis_table.get_item_list_key(id_string), item_string)

	def remove_item(self, redis, id_string, item_string):
		redis.lrem(self.redis_table.get_item_list_key(id_string), 0, item_string)

	def get_friend_list(self, redis, id_string):
		return redis.lrange(self.redis_table.get_friend_list_key(id_string), 0, -1)

	def get_friend_dict_list(self, redis, id_string):
		friend_string_list = self.get_friend_list(redis, id_string)
		friend_dict_list = []
		with redis.pipeline() as pipe:
			for friend_string in friend_string_list:
				pipe.hgetall(self.redis_table.get_friend_key(id_string, friend_string))
			friend_dict_list = pipe.execute()
		return friend_dict_list

	def add_friend(self, redis, id_string, friend_string, d):
		redis.rpush(self.redis_table.get_friend_list_key(id_string), friend_string)
		redis.hmset(self.redis_table.get_friend_key(id_string, friend_string), d)

	def remove_friend(self, redis, id_string, friend_string):
		redis.lrem(self.redis_table.get_friend_list_key(id_string), 0, friend_string)
		redis.del(self.redis_table.get_friend_key(id_string, friend_string))

	def get_friend(self, redis, id_string, friend_string):
		return redis.hgetall(self.redis_table.get_friend_key(id_string, friend_string))

	def set_friend(self, redis, id_string, friend_string, d):
		redis.hmset(self.redis_table.get_friend_key(id_string, friend_string), d)

	def get_friend_table_user_name(self, redis, id_string, friend_string):
		return redis.hget(
			self.redis_table.get_friend_key(id_string, friend_string),
			self.redis_table.get_friend_table_user_name_field()
			)

	def set_friend_table_user_name(self, redis, id_string, friend_string, user_name_string):
		redis.hset(
			self.redis_table.get_friend_key(id_string, friend_string),
			self.redis_table.get_friend_table_user_name_field(),
			user_name_string
			)

	def get_friend_table_user_id(self, redis, id_string, friend_string):
		return redis.hget(
			self.redis_table.get_friend_key(id_string, friend_string),
			self.redis_table.get_friend_table_user_id_field()
			)

	def set_friend_table_user_id(self, redis, id_string, friend_string, user_id_string):
		redis.hset(
			self.redis_table.get_friend_key(id_string, friend_string),
			self.redis_table.get_friend_table_user_id_field(),
			user_id_string
			)

	def get_online_player_list(self, redis):
		return redis.get(self.redis_table.get_online_player_list_key())

	def add_online_player(self, redis, online_player_string):
		redis.rpush(self.redis_table.get_online_player_list_key(), online_player_string)

	def remove_online_player(self, redis, online_player_string):
		redis.lrem(self.redis_table.get_online_player_list_key(), 0, online_player_string)

	def get_level_rank(self, redis, member_string):
		return redis.zrank(self.redis_table.get_level_rank_key(), member_string)

	def add_level_rank(self, redis, member_string, score):
		redis.zadd(self.redis_table.get_level_rank_key(), score, member_string)

	def remove_level_rank(self, redis, member_string):
		redis.zrem(self.redis_table.get_level_rank_key(), member_string)

	def get_level_rank_range(self, redis, start, stop):
		return redis.zrange(self.redis_table.get_level_rank_key(), start, stop)

	def get_race_score_rank(self, redis, id_string, member_string):
		return redis.zrank(self.redis_table.get_race_score_rank_key(id_string), member_string)

	def add_race_score_rank(self, redis, id_string, member_string, score):
		redis.zadd(self.redis_table.get_race_score_rank_key(id_string), score, member_string)

	def remove_race_score_rank(self, redis, id_string, member_string):
		redis.zrem(self.redis_table.get_race_score_rank_key(id_string), member_string)

	def get_race_score_rank_range(self, redis, id_string, start, stop):
		return redis.zrange(self.redis_table.get_race_score_rank_key(id_string), start, stop)
"""