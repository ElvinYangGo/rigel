from master_server.master_server_initializer import MasterServerInitializer

if __name__ == '__main__':
	print 'master started'

	server_initializer = MasterServerInitializer('tcp://localhost:34510', 'tcp://localhost:34511')
	server_initializer.initialize()
