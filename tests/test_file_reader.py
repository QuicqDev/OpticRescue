"""
test reader random
"""
import random
from opticmedian.utils.file_reader import Filer
from omegaconf import OmegaConf

path = OmegaConf.load("opticmedian/config/optics.yml")
path = path.plyer.EYES.app_icon
print(path)
file = Filer(path)
file_iter, file_index = file.get_random_iter()

print(file_index)
print(file_iter)
for i in range(20):
	num = random.randint(0, file_index-1)
	print(num, file_iter[num])
	print(file_iter[num].replace('\\', '/'))
