import xml.dom.minidom
from common.server_option_config import ServerOptionConfig

class ServerOptionReader:
	def __init__(self, file_name=None, string_content=None):
		self.file_name = file_name
		self.string_content = string_content
		self.server_option_config = None
	
	def parse(self):
		if self.file_name is not None:
			self.parse_file()
		elif self.string_content is not None:
			self.parse_string()
		
	def parse_file(self):
		xmldoc = xml.dom.minidom.parse(self.file_name)
		self.parse_xmldoc(xmldoc)
	
	def parse_string(self):
		xmldoc = xml.dom.minidom.parseString(self.string_content)
		self.parse_xmldoc(xmldoc)
		
	def parse_xmldoc(self, xmldoc):
		root_element_list = xmldoc.getElementsByTagName('config')
		if root_element_list.length != 0:
			root_element = root_element_list[0]
		else:
			return

		heart_beat_interval_element = root_element.getElementsByTagName('heart_beat_interval')[0]
		heart_beat_timeout_element = root_element.getElementsByTagName('heart_beat_timeout')[0]
		heart_beat_interval = int(heart_beat_interval_element.firstChild.data)
		heart_beat_timeout = int(heart_beat_timeout_element.firstChild.data)
		
		self.server_option_config = ServerOptionConfig(heart_beat_interval, heart_beat_timeout)

	def get_server_option_config(self):
		return self.server_option_config
	
if __name__ == '__main__':
	server_option_reader = ServerOptionReader(file_name='../config/server_option.xml')
	server_option_reader.parse()