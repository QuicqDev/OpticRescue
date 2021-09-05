"""
Main class of notification system
"""
import argparse
import random
import sys
import time
from omegaconf import OmegaConf
from plyer import notification
from utils.file_reader import Filer


class Notify:
	"""
	Main Notification payload class
	"""

	def __init__(self, config, time_interval=None, stop_interval=None, app_name=None):
		self.config = OmegaConf.load(config)

		if time_interval is None:
			self.time_interval = self.config.default.TIMEINTERVAL
		else:
			self.time_interval = time_interval

		if stop_interval is None:
			self.stop_iter = self.config.default.STOPINTERTVAL
		else:
			self.stop_iter = stop_interval

		if app_name is not None:
			self.app_name = app_name
		else:
			self.app_name = self.config.plyer.APP_NAME

	def eyes(self):
		"""
		Notification for eyes
		Returns:
			boolean
		"""
		eye_title = self.config.plyer.EYES.title
		eye_message = self.config.plyer.EYES.message
		eye_timeout = self.config.plyer.EYES.timeout
		eye_ticker = self.config.plyer.EYES.ticker
		eye_toast = self.config.plyer.EYES.toast

		eye_icons = self.config.plyer.EYES.app_icon
		file = Filer(eye_icons)
		file_iter, file_index = file.get_random_iter()

		counter = 0
		while True:
			time.sleep(self.time_interval)
			print("Notified")

			num = random.randint(0, file_index - 1)
			icon = file_iter[num]

			# for windows system
			if "win" in sys.platform.lower():
				icon = icon.replace('\\', '/')

			_ = notification.notify(
				title=eye_title,
				message=eye_message,
				app_icon=icon,
				app_name=self.app_name,
				ticker=eye_ticker,
				toast=eye_toast,
				timeout=eye_timeout
			)
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
	optic_fiber = Notify(r"opticmedian/config/optics.yml", time_interval=interval, stop_interval=stop_iterations)
	optic_fiber.eyes()
