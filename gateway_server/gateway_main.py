from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from gateway_server.client_message_relay import ClientMessageRelay
from common.mq_reader import MQReader
from gateway_server.gateway_server_initializer import GatewayServerInitializer
from gateway_server.gateway_handler_register import GatewayHandlerRegister

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_initializer = GatewayServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'gateway_server',
		GatewayHandlerRegister()
		)
	server_initializer.initialize()
	
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	channel_pipeline_factory.append_handler('client_message_relay', ClientMessageRelay())
	
	endpoint = TCP4ServerEndpoint(reactor, 34600)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory))
	reactor.run()
	
	print u'authentication started'
	
