from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher
from common.auto_handler_register import AutoHandlerRegister
from client_sample.connection_handler import ConnectionHandler
from client_sample.client_global_data import ClientGlobalData
import client_sample.msg_sender

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
	ClientGlobalData.twisted_protocol_factory = TwistedProtocolFactory(channel_pipeline_factory, None)

	print u'client started'
	ClientGlobalData.status = 1
	client_sample.msg_sender.connect('localhost', 34500)	

	reactor.run()
