import xml.dom.minidom

class ProtocolIDParser:
	def __init__(self, file_name):
		self.file_name = file_name
		self.id_list = []
		
	def parse(self):
		xmldoc = xml.dom.minidom.parse(self.file_name)
		root_element = xmldoc.getElementsByTagName('protocols')
		if not root_element.length:
			return
		
		protocol_element_list = root_element[0].getElementsByTagName('protocol')
		for protocol_element in protocol_element_list:
			if protocol_element.hasChildNodes():
				self.id_list.append(protocol_element.firstChild.data)

	def get_id_list(self):
		return self.id_list
	
