#!/usr/bin/python3.3
import os.path
import urllib.request

links = open('links.txt', 'r')
for link in links:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join('downloads', name)

    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')