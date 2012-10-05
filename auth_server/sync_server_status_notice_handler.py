from common.server import Server
import protocol.server_message_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from common.global_data import GlobalData
from protocol.server_protocol_id import ServerProtocolID

class SyncServerStatusNoticeHandler:
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE,
			SyncServerStatusNoticeHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.SyncServerNotice.FromString(
			channel_buffer.read_all_data()
			)
		for server_net in message.servers:
			if server_net.status == ServerStatus.SERVER_STATUS_RUNNING:
				self.handle_running_server(server_net)
			elif server_net.status == ServerStatus.SERVER_STATUS_CLOSED:
				self.handle_closed_server(server_net)
				
	def handle_running_server(self, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER or server_net.type == ServerType.GAME_SERVER:
			print '%s running' % (server_net.name)
			server = Server(server_net.name, server_net.type, server_net.status)
			GlobalData.inst.server_manager.add_server(server)
	
	def handle_closed_server(self, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER or server_net.type == ServerType.GAME_SERVER:
			print '%s closed' % (server_net.name)
			GlobalData.inst.server_manager.remove_server(server_net.type, server_net.name)
