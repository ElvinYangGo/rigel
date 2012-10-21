#This file is generated by program. DO NOT EDIT IT MANUALLY!
class ClientProtocolID(object):
	ID_TYPE_MAGIC = 0xff00

	ID_TYPE_CCENTER = 0x0200
	ID_TYPE_CAUTH = 0x0000
	ID_TYPE_CGATEWAY = 0x0100

	#cgame id_start:0x1001
	CGAME_ID_START = 0x1001
	P_CREATE_AVATAR_REQ = 0x1001
	P_CREATE_AVATAR_RES = 0x1002
	R_CREATE_AVATAR_RES_SUCCESS = 0x10020001
	R_CREATE_AVATAR_RES_FAILURE = 0x10020002

	#ccenter id_start:0x0201
	CCENTER_ID_START = 0x0201

	#cauth id_start:0x0001
	CAUTH_ID_START = 0x0001
	P_LOGIN_AUTH_REQ = 0x0001
	P_LOGIN_AUTH_RES = 0x0002
	R_LOGIN_AUTH_RES_SUCCESS = 0x00020001
	R_LOGIN_AUTH_RES_FAILURE = 0x00020002
	R_LOGIN_AUTH_RES_USER_NAME_NOT_EXIST = 0x00020003
	R_LOGIN_AUTH_RES_USER_NAME_OR_PASSWORD_INVALID = 0x00020004
	R_LOGIN_AUTH_RES_NO_GATEWAY_SERVER = 0x00020005
	R_LOGIN_AUTH_RES_NO_GAME_SERVER = 0x00020006
	P_CREATE_ACCOUNT_REQ = 0x0003
	P_CREATE_ACCOUNT_RES = 0x0004
	R_CREATE_ACCOUNT_RES_SUCCESS = 0x00040001
	R_CREATE_ACCOUNT_RES_FAILURE = 0x00040002
	R_CREATE_ACCOUNT_RES_NAME_ALREADY_EXIST = 0x00040003

	#cgateway id_start:0x0101
	CGATEWAY_ID_START = 0x0101
	P_LOGIN_GATEWAY_REQ = 0x0101
	P_LOGIN_GATEWAY_RES = 0x0102
	R_LOGIN_GATEWAY_RES_SUCCESS = 0x01020001
	R_LOGIN_GATEWAY_RES_FAILURE = 0x01020002
	R_LOGIN_GATEWAY_RES_TOKEN_EXPIRED = 0x01020003
	R_LOGIN_GATEWAY_RES_TOKEN_INVALID = 0x01020004
	R_LOGIN_GATEWAY_RES_GAME_SERVER_CLOSED = 0x01020005

