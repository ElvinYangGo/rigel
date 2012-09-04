from generator.plain_class_accessor_generator.plain_list_map_map_accessor_writer import PlainListMapMapAccessorWriter
from generator.plain_class_accessor_generator.plain_list_map_list_accessor_writer import PlainListMapListAccessorWriter

class PlainListMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.plain_list_map_map_accessor_writer = PlainListMapMapAccessorWriter(table_desc, f)
		self.plain_list_map_list_accessor_writer = PlainListMapListAccessorWriter(table_desc, f)

	def write_import_declaration(self):
		self.plain_list_map_map_accessor_writer.write_import_declaration()
		self.plain_list_map_list_accessor_writer.write_import_declaration()

	def write(self):
		self.plain_list_map_map_accessor_writer.write()
		self.plain_list_map_list_accessor_writer.write()

"""
	def get_friend(self, redis, id_int, friend_int):
		friend_dict = self.redis_accessor.get_friend(redis, str(id_int), str(friend_int))
		user_name_param = ''
		if self.redis_key.get_friend_table_user_name_field() in friend_dict:
			user_name_param = friend_dict[self.redis_key.get_friend_table_user_name_field()]
		user_id_param = 0
		if self.redis_key.get_friend_table_user_id_field() in friend_dict:
			user_id_param = int(friend_dict[self.redis_key.get_friend_table_user_id_field()])
		return Friend(user_name=user_name_param, user_id=user_id_param)

	def set_friend(self, redis, id_int, friend_int, friend):
		friend_dict = {}
		friend_dict[self.redis_key.get_friend_table_user_name_field()] = friend.get_user_name()
		friend_dict[self.redis_key.get_friend_table_user_id_field()] = str(friend.get_user_id())
		self.redis_accessor.set_friend(redis, str(id_int), str(friend_int), friend_dict)

	def get_friend_table_user_name(self, redis, id_int, friend_int):
		return self.redis_accessor.get_friend_table_user_name(redis, str(id_int), str(friend_int))

	def set_friend_table_user_name(self, redis, id_int, friend_int, user_name):
		self.redis_accessor.set_friend_table_user_name(redis, str(id_int), str(friend_int), user_name)

	def get_friend_table_user_id(self, redis, id_int, friend_int):
		return int(self.redis_accessor.get_friend_table_user_id(redis, str(id_int), str(friend_int)))

	def set_friend_table_user_id(self, redis, id_int, friend_int, user_id):
		self.redis_accessor.set_friend_table_user_id(redis, str(id_int), str(friend_int), str(user_id))

"""