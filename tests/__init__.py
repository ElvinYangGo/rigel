import os
import sys
import unittest

def get_tests():
	current_directory = os.path.abspath(os.path.dirname(sys.argv[0]))
	suite = unittest.TestSuite()
	for file_name in os.listdir(current_directory):
		if file_name.startswith('test') and file_name.endswith('.py'):
			module_name = file_name[:-3]
			__import__(module_name)
			module = sys.modules[module_name]
			suite.addTest(module.get_tests())

	return suite

if '__main__' == __name__:
	suite = get_tests()
	runner = unittest.TextTestRunner()
	runner.run(suite)
