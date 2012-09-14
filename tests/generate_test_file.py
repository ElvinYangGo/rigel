import sys

#usage: python generate_test_file [package_name] [file_name]

if '__main__' == __name__:
	package_name = sys.argv[1]
	file_name = sys.argv[2]
	
	characters = file_name.split('_')
	class_name = ''
	for s in characters:
		class_name += s[0].upper()
		class_name += s[1:]
	
	test_file = open(package_name + '_tests' + '/test_' + file_name + '.py', 'w')

	test_file.write('import unittest\n')
	test_file.write('import tests.auxiliary\n')
	test_file.write('from mock import Mock\n\n')

	test_file.write('class ' + class_name + 'Test(unittest.TestCase):\n')
	test_file.write('	def setUp(self):\n')
	test_file.write('		pass\n\n')

	test_file.write('def get_tests():\n')
	test_file.write('	return unittest.makeSuite(' + class_name + 'Test)\n\n')

	test_file.write("if '__main__' == __name__:\n")
	test_file.write('	unittest.main()')

	test_file.close()
