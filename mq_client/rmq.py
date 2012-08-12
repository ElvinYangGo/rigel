from mq_client.rmq_pub import RMQPub
from mq_client.rmq_sub import RMQSub

class RMQ(RMQPub, RMQSub):
	def __init__(self, pub_address, sub_address, context, pipeline):
		RMQPub.__init__(self, pub_address, context)
		RMQSub.__init__(self, sub_address, context, pipeline)