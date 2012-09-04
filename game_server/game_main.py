from game_server.game_server_initializer import GameServerInitializer
from common.mq_reader import MQReader
from network.channel_pipeline import ChannelPipeline
from common.handler_dispatcher import HandlerDispatcher
from common.auto_handler_register import AutoHandlerRegister

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = AutoHandlerRegister().register(
		'game_server',
		'.',
		'register_server_handler',
		HandlerDispatcher()
		)
	rmq_pipeline = ChannelPipeline()
	#rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = GameServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'game_server',
		rmq_pipeline,
		'../config/redis_server.json',
		'../config/redis_partition.json'
		)
	server_initializer.initialize()

	"""
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('client_message_handler_dispatcher', ())
	channel_pipeline_factory.append_handler('protocol_wrapper_codec', ())
	channel_pipeline_factory.append_handler('server_message_handler_dispatcher', HandlerDispatcher())
	"""

	print u'game started'
