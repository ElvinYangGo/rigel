from common.mq_reader import MQReader
from center_server.center_server_initializer import CenterServerInitializer
from center_server.center_handler_dispatcher import CenterHandlerRegister
from network.channel_pipeline import ChannelPipeline
from common.handler_dispatcher import HandlerDispatcher

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_handler_dispatcher = CenterHandlerRegister().register(HandlerDispatcher())
	rmq_pipeline = ChannelPipeline()
	#rmq_pipeline.append_handler('server_message_relay', ServerMessageRelay())
	rmq_pipeline.append_handler('handler_dispatcher', server_handler_dispatcher)

	server_initializer = CenterServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'center_server',
		rmq_pipeline
		)
	server_initializer.initialize()

	print u'center started'
