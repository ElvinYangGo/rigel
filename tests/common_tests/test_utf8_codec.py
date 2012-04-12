# -*- coding: utf-8 -*-

import unittest
import tests.auxiliary
from common.utf8_codec import utf8_decode
from common.utf8_codec import utf8_encode 

class UTF8CodecTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_utf8_encode(self):
		self.assertEqual('aaa', utf8_encode('aaa'))
		self.assertEqual('\xe5\x95\x8a', utf8_encode('啊'))
		
	def test_utf8_decode(self):
		self.assertEqual('aaa', utf8_decode('aaa'))
		self.assertEqual('啊', utf8_encode('\xe5\x95\x8a'))

def get_tests():
	return unittest.makeSuite(UTF8CodecTest)

if '__main__' == __name__:
	unittest.main()