# -*- coding: utf-8 -*-

import os
import sys
import unittest
def get_tests(directory, package_name):
	suite = unittest.TestSuite()
	for file_name in os.listdir(directory):
		if file_name.startswith('test') and file_name.endswith('.py'):
			module_name = package_name + '.' + file_name[:-3]
			__import__(module_name)
			module = sys.modules[module_name]
			suite.addTest(module.get_tests())

	return suite

def get_test_suite():
	current_directory = os.path.abspath(os.path.dirname(sys.argv[0]))
	suite = unittest.TestSuite()
	suite.addTest(get_tests(current_directory, ''))
	for name in os.listdir(current_directory):
		if os.path.isdir(name):
			suite.addTest(get_tests(os.path.abspath(name), 'tests.' + name))
	
	return suite

if '__main__' == __name__:
	suite = get_test_suite()
	runner = unittest.TextTestRunner()
	runner.run(suite)
