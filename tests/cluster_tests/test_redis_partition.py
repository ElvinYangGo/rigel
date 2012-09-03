import unittest
import tests.auxiliary
import json
from mock import Mock
from cluster.redis_partition import RedisPartition

class RedisPartitionTest(unittest.TestCase):
	def setUp(self):
		RedisPartition.init_partitions = Mock()
		self.redis_partition = RedisPartition(Mock())

	def test_get_server_name(self):
		json_string = """
[
    {"start":1, "end":100, "server":"s1"},
    {"start":101, "end":200, "server":"s2"}
]"""
		partitions = json.loads(json_string)
		self.redis_partition.partitions = partitions
		self.assertEqual(self.redis_partition.get_server_name(1), 's1')
		self.assertEqual(self.redis_partition.get_server_name(99), 's1')
		self.assertEqual(self.redis_partition.get_server_name(100), 's1')
		self.assertEqual(self.redis_partition.get_server_name(101), 's2')
		self.assertEqual(self.redis_partition.get_server_name(201), None)

def get_tests():
	return unittest.makeSuite(RedisPartitionTest)

if '__main__' == __name__:
	unittest.main()