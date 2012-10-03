import sys
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from client_sample.client_global_data import ClientGlobalData
from protocol.client_protocol_id import ClientProtocolID
import protocol.client_message_pb2

def printError(failure):
	sys.stderr.write(str(failure))
	reactor.stop()
	
def connect(ip, port):
	endpoint = TCP4ClientEndpoint(reactor, ip, port, 5)
	d = endpoint.connect(ClientGlobalData.twisted_protocol_factory)
	d.addErrback(printError)
	
def send_login_auth_message():
	request = protocol.client_message_pb2.LoginAuthReq()
	request.name = 'aaa'
	request.password = 'ppp'
	request.user_token = 'ttt'
	ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_LOGIN_AUTH_REQ)

def send_login_gateway_message(account_id, token):
	request = protocol.client_message_pb2.LoginGatewayReq()
	request.account_id = account_id
	request.token = token
	ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_LOGIN_GATEWAY_REQ)

def create_account():
	request = protocol.client_message_pb2.CreateAccountReq()
	request.name = 'aaa'
	request.password = 'ppp'
	ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_CREATE_ACCOUNT_REQ)

def create_avatar():
	request = protocol.client_message_pb2.CreateAvatarReq()
	request.name = 'aaa'
	request.gender = 1
	request.level = 1
	ClientGlobalData.channel.send_string(request.SerializeToString(), ClientProtocolID.P_CREATE_AVATAR_REQ)
