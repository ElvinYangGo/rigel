from game_server.game_server_initializer import GameServerInitializer
from common.mq_config import MQConfig
from network.channel_pipeline import ChannelPipeline
from common.handler_dispatcher import HandlerDispatcher
from common.auto_handler_register import AutoHandlerRegister
from common.protocol_wrapper_handler import ProtocolWrapperHandler

if __name__ == '__main__':
	mq_config = MQConfig(config_file_name='../config/mq.json')

	handler_register = AutoHandlerRegister()
	server_handler_dispatcher = HandlerDispatcher()
	server_handler_dispatcher = handler_register.register(
		'game_server',
		'.',
		'register_server_handler',
		server_handler_dispatcher
		)
	
	client_handler_dispatcher = HandlerDispatcher()
	client_handler_dispatcher = handler_register.register(
		'game_server',
		'.',
		'register_client_handler',
		client_handler_dispatcher
		)
	protocol_wrapper_handler = ProtocolWrapperHandler(client_handler_dispatcher)
	rmq_pipeline = ChannelPipeline()
	rmq_pipeline.append_handler('protocol_wrapper_handler', protocol_wrapper_handler)
	rmq_pipeline.append_handler('server_handler_dispatcher', server_handler_dispatcher)

	server_initializer = GameServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'game_server',
		rmq_pipeline,
		'../config/redis_server.json',
		'../config/redis_partition.json',
		'../config/server_option.json'
		)
	server_initializer.initialize()

	"""
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('client_message_handler_dispatcher', ())
	channel_pipeline_factory.append_handler('protocol_wrapper_codec', ())
	channel_pipeline_factory.append_handler('server_message_handler_dispatcher', HandlerDispatcher())
	"""

	print u'game started'
