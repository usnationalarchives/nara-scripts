# This script requires Wand for Python. Install using the documentation at http://docs.wand-py.org/en/0.4.1/index.html before running.

import sys, os, datetime
from wand.image import Image

for item in os.listdir(os.getcwd()):
	if item.endswith(".pdf"):
		start = datetime.datetime.now()
		with Image(filename=item) as readpdf:
			pages = len(readpdf.sequence)
			folder = os.getcwd() + '/' + item[:-4]
			if not os.path.exists(folder):
				os.makedirs(folder)
			jpgfile = folder + '/' + item[:-4] + '.jpg'
			readpdf.save(filename=jpgfile)
		os.rename(item, folder + '/' + item)
		end = datetime.datetime.now()
		print 'Took ' + str(int(round((end - start).total_seconds()))) + ' seconds for "' + item + '" (' + str(pages) + ' page(s)).'