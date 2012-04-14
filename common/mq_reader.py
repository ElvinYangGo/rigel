import xml.dom.minidom
from common.mq_config import MQConfig

class MQReader:
	def __init__(self, file_name=None, string_content=None):
		self.file_name = file_name
		self.string_content = string_content
		self.mq_config_list = []
	
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

		mq_element_list = root_element.getElementsByTagName('mq')
		for mq_element in mq_element_list:
			mq_config = self.parse_mq_element(mq_element)
			if mq_config is not None:
				self.mq_config_list.append(mq_config)

	def parse_mq_element(self, mq_element):
		pub_address_element = mq_element.getElementsByTagName('pub_address')[0]
		sub_address_element = mq_element.getElementsByTagName('sub_address')[0]
		if pub_address_element.hasChildNodes() and sub_address_element.hasChildNodes():
			return MQConfig(pub_address_element.firstChild.data, sub_address_element.firstChild.data)
		else:
			return None
	
	def get_mq_config_list(self):
		return self.mq_config_list
	
if __name__ == '__main__':
	mqReader = MQReader(file_name='../config/mq.xml')
	mqReader.parse()