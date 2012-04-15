from master_server.master_server_initializer import MasterServerInitializer
from common.mq_reader import MQReader
from master_server.handler_register import HandlerRegister

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_initializer = MasterServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'master_server',
		HandlerRegister()
		)
	server_initializer.initialize()

	print u'master started'
