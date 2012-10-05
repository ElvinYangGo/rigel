from master_server.master_server_initializer import MasterServerInitializer
from common.mq_reader import MQReader
from common.handler_dispatcher import HandlerDispatcher
from network.channel_pipeline import ChannelPipeline
from common.auto_handler_register import AutoHandlerRegister

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = AutoHandlerRegister().register(
		'master_server',
		'.',
		'register_server_handler',
		HandlerDispatcher()
		)
	rmq_pipeline = ChannelPipeline()
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = MasterServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'master_server',
		rmq_pipeline,
		'../config/redis_server.json',
		'../config/redis_partition.json',
		'../config/server_option.json'
		)
	server_initializer.initialize()

	print u'master started'
