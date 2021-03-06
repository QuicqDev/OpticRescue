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
	def __init__(self, conf_path, time_interval=None, stop_interval=None):
		self.config = OmegaConf.load(conf_path)
		self.appid = self.config.default.AUMID
		self.xml_dom = self.config.default.XMLCONTENT
		if time_interval is None:
			self.time_interval = self.config.default.TIMEINTERVAL
		else:
			self.time_interval = time_interval

		if stop_interval is None:
			self.stop_iter = self.config.default.STOPINTERTVAL
		else:
			self.stop_iter = stop_interval

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

		counter = 0
		while True:
			time.sleep(self.time_interval)
			print("Notified")
			notifier.show(notifications.ToastNotification(x_doc))
			counter += 1
			if counter > self.stop_iter:
				break


def parse_args():
	"""
	argument parser
	:return:
	"""
	parser = argparse.ArgumentParser("Optic Rescue Activate")
	parser.add_argument("--interval", default=1200, type=int, help="Time interval for notifications in secs")
	parser.add_argument("--stop_iterations", type=int, default=1000, help="Stop after this many iterations")

	return parser.parse_args()


if __name__ == "__main__":
	args = parse_args()
	interval = args.interval
	stop_iterations = args.stop_iterations
	optic_fiber = Optic("config/optics.yml", time_interval=interval, stop_interval=stop_iterations)
	optic_fiber.push_notification()
