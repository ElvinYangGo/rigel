# -*- coding: utf-8 -*-

import sys

def set_utf8_default_encoding():
	if sys.getdefaultencoding() != 'utf-8':
		reload(sys)
		sys.setdefaultencoding('utf-8')

def utf8_encode(s):
	set_utf8_default_encoding()
	return s.encode('utf-8')

def utf8_decode(s):
	set_utf8_default_encoding()
	return s.decode('utf-8')