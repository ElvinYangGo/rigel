from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from gateway_server.client_message_relay import ClientMessageRelay

if __name__ == '__main__':
	print 'started'
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	channel_pipeline_factory.append_handler('client_message_relay', ClientMessageRelay())
	
	endpoint = TCP4ServerEndpoint(reactor, 34600)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory))
	reactor.run()
