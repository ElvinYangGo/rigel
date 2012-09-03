import unittest
import tests.auxiliary
from mock import Mock
from cluster.redis_server import RedisServer

class RedisServerTest(unittest.TestCase):
	def setUp(self):
		self.init_servers_mock = Mock()
		RedisServer.init_servers = self.init_servers_mock
		self.redis_server = RedisServer(Mock())

	def test_get_redis(self):
		s1 = Mock()
		s2 = Mock()
		self.redis_server.servers['s1'] = s1
		self.redis_server.servers['s2'] = s2
		self.assertEqual(self.redis_server.get_redis('s1'), s1)
		self.assertEqual(self.redis_server.get_redis('a'), None)

def get_tests():
	return unittest.makeSuite(RedisServerTest)

if '__main__' == __name__:
	unittest.main()