from master_server.server_in_master import ServerInMaster
import protocol.server_message_pb2
from common.server_manager import ServerManager
from common.server_status import ServerStatus

class MasterServerManager(ServerManager):
	def __init__(self):
		super(MasterServerManager, self).__init__()
		
	def add_server(self, name, server_type, status=ServerStatus.SERVER_STATUS_RUNNING):
		if self.servers.has_key(name):
			self.servers[name].clear()
		else:
			server = ServerInMaster(name, server_type)
			self.servers[name] = server
		
	def get_server(self, name):
		return self.servers.get(name)
	
	def to_net(self):
		server_message_list = [server.to_net() for server in self.servers.itervalues()]
		sync_server_notice_message = protocol.server_message_pb2.SyncServerNotice()
		sync_server_notice_message.servers.extend(server_message_list)
		return sync_server_notice_message
		
	def get_all_servers(self):
		return self.servers