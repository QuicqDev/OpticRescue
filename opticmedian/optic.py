"""
head file
"""

from omegaconf import OmegaConf
import xml.etree.ElementTree as ET

import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom


class Optic:
	"""
	head class
	"""
	def __init__(self, conf_path):
		self.config = OmegaConf.load(conf_path)
		self.appid = self.config.default.AUMID
		self.xml_dom = self.config.default.XMLCONTENT

	def read_conf(self):
		"""
		:return:
		"""
		print(self.config)
		print(self.appid)
		print(self.xml_dom, type(self.xml_dom))

	def push_notification(self):
		"""
		:return:
		"""
		notification_manager = notifications.ToastNotificationManager
		notifier = notification_manager.create_toast_notifier(self.appid)
		x_doc = dom.XmlDocument()
		x_doc.load_xml(self.xml_dom)

		notifier.show(notifications.ToastNotification(x_doc))



if __name__ == "__main__":
	optic_fiber = Optic("config/optics.yml")
	optic_fiber.push_notification()
