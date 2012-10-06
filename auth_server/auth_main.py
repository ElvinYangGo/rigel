from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from auth_server.auth_server_initializer import AuthServerInitializer
from common.mq_config import MQConfig
from network.channel_pipeline import ChannelPipeline
from common.auto_handler_register import AutoHandlerRegister

if __name__ == '__main__':
	mq_config = MQConfig(config_file_name='../config/mq.json')

	server_handler_dispatcher = AutoHandlerRegister().register(
		'auth_server',
		'.',
		'register_server_handler',
		HandlerDispatcher()
		)
	rmq_pipeline = ChannelPipeline()
	#rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = AuthServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'auth_server',
		rmq_pipeline,
		'../config/redis_server.json',
		'../config/redis_partition.json',
		'../config/gateway_address.json',
		'../config/server_option.json'
		)
	server_initializer.initialize()
	
	client_handler_dispatcher = AutoHandlerRegister().register(
		'auth_server',
		'.',
		'register_client_handler',
		HandlerDispatcher()
		)
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('handler_dispatcher', client_handler_dispatcher)
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	
	endpoint = TCP4ServerEndpoint(reactor, 34500)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory, None))
	
	print u'auth server started'
	
	reactor.run()