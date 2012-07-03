import json
from generator.redis_table_writer import RedisTableWriter
from generator.redis_accessor_generator.redis_accessor_writer import RedisAccessorWriter
from generator.plain_class_generator.plain_table_array_writer import PlainTableArrayWriter
from generator.plain_class_accessor_generator.plain_class_accessor_writer import PlainClassAccessorWriter

if __name__ == '__main__':
	f = open('data.rd')
	table_desc_array = json.load(f)
	for table_desc in table_desc_array:
		print table_desc

	redis_table_writer = RedisTableWriter('../redis_client/redis_table.py', table_desc_array)
	redis_table_writer.write()
	redis_accessor_writer = RedisAccessorWriter('../redis_client/redis_accessor.py', table_desc_array)
	redis_accessor_writer.write()
	plain_table_array_writer = PlainTableArrayWriter('../plain_class/', table_desc_array)
	plain_table_array_writer.write()
	plain_class_accessor_writer = PlainClassAccessorWriter('../plain_class/plain_class_accessor.py', table_desc_array)
	plain_class_accessor_writer.write()

	print 'finished'
