import protocol.server_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from common.global_data import GlobalData
from common.channel_name import ChannelName

class InitServerReqHandler:
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_INIT_SERVER_REQ,
			InitServerReqHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.InitServerReq.FromString(
			channel_buffer.read_all_data()
			)

		GlobalData.inst.server_manager.add_server(message.name, message.type)
		print '%s, running' % (message.name)
		
		GlobalData.inst.rmq.send_channel_buffer(
			None, message.name, ServerProtocolID.P_INIT_SERVER_RES
			)

		self.send_other_servers_to_this_server(message.name)
		server = GlobalData.inst.server_manager.get_server(message.name)
		self.send_this_server_to_other_servers(server)

	def send_other_servers_to_this_server(self, this_server_name):
		server_list_message = GlobalData.inst.server_manager.to_net()
		GlobalData.inst.rmq.send_message(
			server_list_message, this_server_name, ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)

	def send_this_server_to_other_servers(self, this_server):
		this_server_message = protocol.server_message_pb2.SyncServerNotice()
		this_server_message.servers.extend([this_server.to_net()])
		GlobalData.inst.rmq.send_message(
			this_server_message, ChannelName.SERVER_STATUS, ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)