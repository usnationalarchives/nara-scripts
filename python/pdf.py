# This script is adapted from the code at http://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html

# To use this, simply run the script from the same directory as the PDFs. The script finds all documents in the folder ending in ".pdf" and extracts JPGs from them. This method may only work reliably on scanned documents, which will have a single source image per page.

# The script is currently set up to create a "PDFs" subfolder to save all outputs to.

import sys, os

for item in os.listdir(os.getcwd()):
	n = 1
	if item.endswith(".pdf"):

		pdf = file(item, "rb").read()

		startmark = "\xff\xd8"
		startfix = 0
		endmark = "\xff\xd9"
		endfix = 2
		i = 0

		njpg = 0
		while True:
			istream = pdf.find("stream", i)
			if istream < 0:
				break
			istart = pdf.find(startmark, istream, istream+20)
			if istart < 0:
				i = istream+20
				continue
			iend = pdf.find("endstream", istart)
			if iend < 0:
				raise Exception("Didn't find end of stream!")
			iend = pdf.find(endmark, iend-20)
			if iend < 0:
				raise Exception("Didn't find end of JPG!")

			istart += startfix
			iend += endfix
			print "JPG %d from %d to %d" % (njpg, istart, iend)
			jpg = pdf[istart:iend]
			if not os.path.exists(os.getcwd() + '/PDFs'):
				os.makedirs(os.getcwd() + '/PDFs')
			jpgfile = file(os.getcwd() + "/PDFs/" + item[:-4] + "_(" + str(n) + ").jpg" % njpg, "wb")
			jpgfile.write(jpg)
			jpgfile.close()
	 
	 		n = n + 1
			njpg += 1
			i = iend