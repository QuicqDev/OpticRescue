"""
head file
"""

import time
import argparse

from omegaconf import OmegaConf
import xml.etree.ElementTree as ET

import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom


class Optic:
	"""
	head class
	"""
	def __init__(self, conf_path, time_interval=None):
		self.config = OmegaConf.load(conf_path)
		self.appid = self.config.default.AUMID
		self.xml_dom = self.config.default.XMLCONTENT
		if time_interval is None:
			self.time_interval = self.config.default.TIMEINTERVAL
		else:
			self.time_interval = time_interval

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

		start_time = time.time()
		while True:
			end_time = time.time()
			if end_time - start_time > self.time_interval:
				print("Notified")
				notifier.show(notifications.ToastNotification(x_doc))
				start_time = time.time()


def parse_args():
	"""
	argument parser
	:return:
	"""
	parser = argparse.ArgumentParser("Optic Rescue Activate")
	parser.add_argument("--interval", default=1200, type=int, help="Time interval for notifications")
	parser.add_argument("--stop", type=int, default=100)

	return parser.parse_args()


if __name__ == "__main__":
	args = parse_args()
	time_interval = args.interval
	optic_fiber = Optic("config/optics.yml", time_interval=time_interval)
	optic_fiber.push_notification()
