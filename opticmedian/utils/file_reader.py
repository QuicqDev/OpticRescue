"""
class to read files in specific ways
"""
import glob
import random


class Filer:
	"""
	read files
	"""

	def __init__(self, file_path):
		self.path = file_path

	def get_random_iter(self):
		"""
		get file contents in random
		"""
		nb_files = sum(1 for _ in glob.iglob(self.path))
		file_iter = glob.glob(self.path)

		return file_iter, nb_files


