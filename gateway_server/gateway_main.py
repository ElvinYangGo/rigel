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
from gateway_server.gateway_handler_register import GatewayHandlerRegister
from common.global_data import GlobalData

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = GatewayHandlerRegister().register(HandlerDispatcher())
	rmq_pipeline = ChannelPipeline()
	rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = GatewayServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'gateway_server',
		rmq_pipeline
		)
	server_initializer.initialize()
	
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('client_message_relay', ClientMessageRelay())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	
	endpoint = TCP4ServerEndpoint(reactor, 34600)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory, GlobalData.instance.channel_manager))
	reactor.run()
	
	print u'authentication started'
	
