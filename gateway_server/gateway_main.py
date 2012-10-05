from network.channel_pipeline import ChannelPipeline
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from gateway_server.client_message_relay import ClientMessageRelay
from gateway_server.server_message_relay import ServerMessageRelay
from common.mq_reader import MQReader
from gateway_server.gateway_server_initializer import GatewayServerInitializer
from common.global_data import GlobalData
from common.auto_handler_register import AutoHandlerRegister

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = AutoHandlerRegister().register(
		'gateway_server',
		'.',
		'register_server_handler',
		HandlerDispatcher()
		)
	rmq_pipeline = ChannelPipeline()
	rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = GatewayServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'gateway_server',
		rmq_pipeline,
		'../config/redis_server.json',
		'../config/redis_partition.json'
		)
	server_initializer.initialize()

	client_handler_dispatcher = AutoHandlerRegister().register(
		'gateway_server',
		'.',
		'register_client_handler',
		HandlerDispatcher()
		)
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('client_message_relay', ClientMessageRelay())
	channel_pipeline_factory.append_handler('handler_dispatcher', client_handler_dispatcher)
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())

	endpoint = TCP4ServerEndpoint(reactor, 34600)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory, GlobalData.inst.channel_manager))
	
	print u'gateway started'
	
	reactor.run()