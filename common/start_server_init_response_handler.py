from common.heart_beat import HeartBeat
import xml.dom.minidom
from common.server_option_reader import ServerOptionReader
from common.global_data import GlobalData

class StartServerInitResponseHandler:
	def __init__(self):
		pass

	def has_config(self, config, config_name):
		xmldoc = xml.dom.minidom.parseString(config)
		root_element_list = xmldoc.getElementsByTagName(u'config')
		if root_element_list.length != 0:
			root_element = root_element_list[0]
		else:
			return False
		
		config_element_list = root_element.getElementsByTagName(config_name)
		if config_element_list.length == 0:
			return False
		
		return True
	
	def get_config_string(self, config, config_name):
		xmldoc = xml.dom.minidom.parseString(config)
		root_element_list = xmldoc.getElementsByTagName(u'config')
		if root_element_list.length != 0:
			root_element = root_element_list[0]
		else:
			return None
		
		outter_config_element_list = root_element.getElementsByTagName(config_name)
		if outter_config_element_list.length == 0:
			return None
		
		inner_config_element_list = outter_config_element_list[0].getElementsByTagName(u'config')
		config_element = inner_config_element_list[0]
		return config_element.toxml('utf-8')

	def init_heart_beat(self, server_option_config):
		heart_beat_interval = server_option_config.get_heart_beat_interval()
		if not hasattr(GlobalData.instance, u'heart_beat'):
			GlobalData.instance.heart_beat = HeartBeat(heart_beat_interval)
			GlobalData.instance.heart_beat.start()
		else:
			GlobalData.instance.heart_beat.set_heart_beat_interval(heart_beat_interval)
	
	def get_server_option_reader(self, config):
		server_option_string = self.get_config_string(config, u'server_option_config')
		server_option_reader = ServerOptionReader(string_content=server_option_string)
		server_option_reader.parse()
		
		return server_option_reader
	