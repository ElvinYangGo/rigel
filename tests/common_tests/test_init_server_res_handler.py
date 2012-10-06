import unittest
import tests.auxiliary
from common.init_server_res_handler import InitServerResHandler
from mock import Mock
from common.global_data import GlobalData
import common.init_server_res_handler
from common.server_status import ServerStatus

class InitServerResHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = InitServerResHandler()

	def test_init_heart_beat(self):
		common.init_server_res_handler.HeartBeat = Mock()
		common.init_server_res_handler.HeartBeat.return_value = Mock()
		common.init_server_res_handler.HeartBeat.return_value.start = Mock()
		GlobalData.inst = Mock()
		GlobalData.inst.server_option_config = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_interval = Mock()
		GlobalData.inst.server_option_config.get_heart_beat_interval.return_value = 3
		self.handler.init_heart_beat()
		common.init_server_res_handler.HeartBeat.assert_called_with(3)
		self.assertTrue(common.init_server_res_handler.HeartBeat.return_value.start.called)

	def test_handle_message(self):
		GlobalData.inst = GlobalData()
		self.handler.init_heart_beat = Mock()
		self.handler.handle_message(
			111,
			Mock()
			)
		self.assertTrue(self.handler.init_heart_beat.called)
		self.assertEqual(GlobalData.inst.server_status, ServerStatus.SERVER_STATUS_RUNNING)

def get_tests():
	return unittest.makeSuite(InitServerResHandlerTest)

if '__main__' == __name__:
	unittest.main()