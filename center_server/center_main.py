from common.mq_reader import MQReader
from center_server.center_server_initializer import CenterServerInitializer
from center_server.center_handler_dispatcher import CenterHandlerRegister
from center_server.center_global_data import CenterGlobalData

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_initializer = CenterServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'center_server',
		CenterHandlerRegister(),
		CenterGlobalData
		)
	server_initializer.initialize()

	print u'center started'
