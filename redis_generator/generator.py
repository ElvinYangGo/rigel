import json
from redis_generator.redis_table_writer import RedisTableWriter
from redis_generator.redis_accessor_writer import RedisAccessorWriter

"""
friend:user_id

friend:friend_id
user_id
user_name
"""


if __name__ == '__main__':
	f = open('data.rd')
	table_desc_array = json.load(f)
	for table_desc in table_desc_array:
		print table_desc

	redis_table_writer = RedisTableWriter('../redis_client/redis_table.py', table_desc_array)
	redis_table_writer.write()
	redis_accessor_writer = RedisAccessorWriter('../redis_client/redis_accessor.py', table_desc_array)
	redis_accessor_writer.write()

	print 'finished'
