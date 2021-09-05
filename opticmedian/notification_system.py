"""
Main class of notification system
"""

import glob
import time
from omegaconf import OmegaConf
from plyer import notification

title = "Time to relax your EYES"
message = "Relax your eyes"
app_name = "python"
timeout = 12
ticker = "Notification ticker"
app_icon = r"../statics/Icons/eyes_on_fire.ico"
toast = False

notifications = notification.notify(
	title=title,
	message=message,
	app_icon=app_icon,
	app_name=app_name,
	ticker=ticker,
	toast=toast
)
