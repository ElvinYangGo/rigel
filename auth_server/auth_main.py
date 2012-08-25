from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from auth_server.auth_server_initializer import AuthServerInitializer
from common.mq_reader import MQReader
from auth_server.auth_handler_register import AuthHandlerRegister
from network.channel_pipeline import ChannelPipeline
from common.global_data import GlobalData

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = AuthHandlerRegister().register(HandlerDispatcher())
	rmq_pipeline = ChannelPipeline()
	#rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = AuthServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'auth_server',
		rmq_pipeline
		)
	server_initializer.initialize()
	
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	
	endpoint = TCP4ServerEndpoint(reactor, 34500)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory, GlobalData.instance.channel_manager))
	reactor.run()
	
	print u'auth server started'
	
