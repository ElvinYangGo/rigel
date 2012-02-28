import sys

if '__main__' == __name__:
	file_name = sys.argv[1]
	
	characters = file_name.split('_')
	class_name = ''
	for s in characters:
		class_name += s[0].upper()
		class_name += s[1:]
	
	test_file = open('test_' + file_name + '.py', 'w')

	test_file.write('import unittest\n')
	test_file.write('import tests.auxiliary\n\n')

	test_file.write('class ' + class_name + 'Test(unittest.TestCase):\n')
	test_file.write('	def setUp(self):\n')
	test_file.write('		pass\n\n')

	test_file.write('def get_tests():\n')
	test_file.write('	return unittest.makeSuite(' + class_name + 'Test)\n\n')

	test_file.write("if '__main__' == __name__:\n")
	test_file.write('	unittest.main()')

	test_file.close()
