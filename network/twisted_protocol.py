from twisted.internet.protocol import Protocol

class TwistedProtocol(Protocol):
	def __init__(self, channel):
		channel.set_twisted_protocol(self)
		self.channel = channel
		
	def connectionMade(self):
		self.channel.handle_connection()
	
	def connectionLost(self, reason):
		self.channel.handle_disconnection()
		
	def dataReceived(self, data):
		self.channel.appen_data(data)

	def get_remote_ip(self):
		return self.transport.getPeer().host;
	
	def get_remote_port(self):
		return self.transport.getPeer().port;