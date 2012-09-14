import protocol.client_message_pb2
from auth_server.auth_global_data import AuthGlobalData
from protocol.client_protocol_id import ClientProtocolID
from common.util import send_result
from plain_class.user import User

class CreateAccountHandler(object):
	@staticmethod
	def register_client_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ClientProtocolID.P_CREATE_ACCOUNT_REQ,
			CreateAccountHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		channel = kwargs['channel']
		request = protocol.client_message_pb2.CreateAccountReq.FromString(
			channel_buffer.read_all_data()
			)
		response = protocol.client_message_pb2.CreateAccountRes()

		#check if this name exist
		if self.name_exist(request):
			send_result(
				channel,
				response,
				ClientProtocolID.P_CREATE_ACCOUNT_RES,
				ClientProtocolID.R_CREATE_ACCOUNT_RES_NAME_ALREADY_EXIST
				)
			return

		self.create_account(request)

		#send result to client
		send_result(
			channel,
			response,
			ClientProtocolID.P_CREATE_ACCOUNT_RES,
			ClientProtocolID.R_CREATE_ACCOUNT_RES_SUCCESS
			)

	def name_exist(self, request):
		result = AuthGlobalData.inst.plain_class_accessor.setnx_user_name_to_id(
			AuthGlobalData.inst.redis_cluster.get_account_redis(),
			request.name,
			0
			)
		#if hsetnx return 1, the name does not exist
		if result == 1:
			return False
		else:
			return True 

	def create_account(self, request):
		#get an account id from redis
		r = AuthGlobalData.inst.redis_cluster.get_account_redis()
		account_id = AuthGlobalData.inst.plain_class_accessor.incr_account_id(r)
		#save user to redis
		AuthGlobalData.inst.plain_class_accessor.set_user_name_to_id(r, request.name, account_id)
		user = User(account_id, request.name, request.password)
		AuthGlobalData.inst.plain_class_accessor.set_user(r, account_id, user)
