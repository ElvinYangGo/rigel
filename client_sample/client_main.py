from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from common.auto_handler_register import AutoHandlerRegister
from client_sample.connection_handler import ConnectionHandler

if __name__ == '__main__':
	client_handler_dispatcher = AutoHandlerRegister().register(
		'client_sample',
		'.',
		'register_client_handler',
		HandlerDispatcher()
		)
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('handler_dispatcher', client_handler_dispatcher)
	channel_pipeline_factory.append_handler('connection_handler', ConnectionHandler())
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())

	def printError(failure):
		import sys
		sys.stderr.write(str(failure))
		reactor.stop()
	print u'client started'
	endpoint = TCP4ClientEndpoint(reactor, 'localhost', 34500, 5)
	d = endpoint.connect(TwistedProtocolFactory(channel_pipeline_factory, None))
	d.addErrback(printError)
	reactor.run()
