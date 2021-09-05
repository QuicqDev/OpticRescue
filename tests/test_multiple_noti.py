"""
batch notifications
"""
import glob
import time
from omegaconf import OmegaConf
from plyer import notification
import time

title = "Time to relax your EYES"
message = "Relax your eyes"
app_name = "Opticcca"
timeout = 2
ticker = "Notification ticker"
app_icon = r"../statics/Icons/eyes/eyes_on_fire.ico"
toast = False

for i in range(5):
	time.sleep(5)
	notifications = notification.notify(
		title=title,
		message=message,
		app_icon=app_icon,
		app_name=app_name,
		ticker=ticker,
		toast=toast
	)