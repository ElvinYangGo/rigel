from common.server_type import ServerType
from auth_server.server_dispatcher import ServerDispatcher

class AuthServerManager:
	def __init__(self):
		self.dispatchers = {}
		self.dispatchers[ServerType.GAME_SERVER] = ServerDispatcher(ServerType.GAME_SERVER)
		self.dispatchers[ServerType.GATEWAY_SERVER] = ServerDispatcher(ServerType.GATEWAY_SERVER)
		
	def contain_server(self, server_type, name):
		dispatcher = self.dispatchers.get(server_type)
		if dispatcher:
			return dispatcher.contain_server(name)
		return False

	def add_server(self, server):
		dispatcher = self.dispatchers.get(server.get_type())
		if dispatcher:
			dispatcher.add_server(server)
		
	def remove_server(self, server_type, name):
		dispatcher = self.dispatchers.get(server_type)
		if dispatcher:
			dispatcher.remove_server(name)
	
	def dispatch_server(self, server_type):
		dispatcher = self.dispatchers.get(server_type)
		if dispatcher:
			return dispatcher.dispatch_server()
		return None
			