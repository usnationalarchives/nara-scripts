# This script requires Wand for Python. Install using the documentation at http://docs.wand-py.org/en/0.4.1/index.html before running.

import sys, os, datetime
from wand.image import Image

for item in os.listdir(os.getcwd()):
	if item.endswith(".pdf"):
		start = datetime.datetime.now()
		with Image(filename=item) as readpdf:
			pages = len(readpdf.sequence)
			if not os.path.exists(os.getcwd() + '/PDFs'):
				os.makedirs(os.getcwd() + '/PDFs')
			jpgfile = os.getcwd() + "/PDFs/" + item[:-4] + ".jpg"
			readpdf.save(filename=jpgfile)
		end = datetime.datetime.now()
		print 'Took ' + str(int(round((end - start).total_seconds()))) + ' seconds for "' + item + '" (' + str(pages) + ' page(s)).'