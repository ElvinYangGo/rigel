from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from authentication_server.authentication_server_initializer import AuthenticationServerInitializer

if __name__ == '__main__':
	print 'started'
	
	server_initializer = AuthenticationServerInitializer('localhost:34510', 'localhost:34511')
	server_initializer.initialize()
	
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	
	endpoint = TCP4ServerEndpoint(reactor, 34500)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory))
	reactor.run()
	
	print 'authentication started'
	
