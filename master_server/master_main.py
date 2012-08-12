from master_server.master_server_initializer import MasterServerInitializer
from common.mq_reader import MQReader
from master_server.master_handler_register import MasterHandlerRegister
from common.server_option_reader import ServerOptionReader
from common.handler_dispatcher import HandlerDispatcher
from network.channel_pipeline import ChannelPipeline

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_option_reader = ServerOptionReader('../config/server_option.xml')
	server_option_reader.parse()
	
	server_handler_dispatcher = MasterHandlerRegister().register(HandlerDispatcher())
	rmq_pipeline = ChannelPipeline()
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = MasterServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'master_server',
		rmq_pipeline,
		server_option_reader
		)
	server_initializer.initialize()

	print u'master started'
