from os import walk

import sys
import numpy as np
import pickle



def get_data_set(name = "train",normalize = False):
	x = []
	y = []
	l = ["agriculture", "building", "tree", "water"]

	folder_name = "../inputs/merged/"

	if name == "train":
		files = []
		dirs = []
		for (dirpath, dirnames, filenames) in walk(folder_name):
			dirs.extend(dirnames)
			files.extend(filenames)

		for i,file_name in enumerate(files):
			y_class = []
			# read data
			data = np.load(folder_name + dirs[i] + "/" + file_name)
			
			reshaped = []

			for d in data:
				reshaped.append(d.flatten())
				y_row = np.zeros(len(dirs))
				y_row[i] = 1
				y_class.append(y_row)
			y.extend(y_class)
			x.extend(reshaped)
			
			# create labels
			
	# normalzie numpy matrix
	def nomalize(x):
		return (x - x.min()) / (x.max()-x.min())
	if normalize:
		x = normalize(x)
	

	return np.array(x), np.array(y), l
