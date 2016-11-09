import csv, requests, json, re

with open('amara.csv', 'wb') as write :
	writelog = csv.writer(write, delimiter= '\t', quoting=csv.QUOTE_ALL)
	writelog.writerow( ('num', 'visible', 'NAID', 'id', 'language', 'url' ) )
write.closed

offset = 0
try:
	while offset < 300:

		amara  = json.loads(requests.get('https://amara.org/api/videos/?format=json&limit=100&offset=' + str(offset) + '&team=national-archives', headers= {'X-api-username': 'dominic.Byrd-McDevitt@nara.gov', 'X-api-key': 'fdd058617f6da2392a4e357f557527002eaaa756'}).text)
		print amara
		video = 0
		lang = 0
		while video < 100:
			
			num = int(video) + int(offset) + 1
			id = amara['objects'][video]['id']
			
			description = re.search('(National Archives Identifier:|Cod de identificare la National Archives:) *([0-9]{4,8})', amara['objects'][video]['description'], flags = re.MULTILINE)
			try:
				naid = description.group(2)
			except AttributeError:
				naid = 'NO NAID FOUND'
				print 'https://amara.org/api/videos/' + id + '/?format=json'
				print amara['objects'][video]['description']
				
			try:
				visible = str(amara['objects'][video]['languages'][lang]['visible'])
				language = amara['objects'][video]['languages'][lang]['code']
				
			except:
				video = video + 1
				continue
			try:
				if amara['objects'][video]['languages'][int(lang + 1)]['code']:
					lang = lang + 1
					video = video - 1
			except:
				lang = 0
				
			api_url = 'https://amara.org/api/videos/' + id + '/languages/' + language + '/subtitles/?format=json'

			with open('amara.csv', 'a') as write :
				writelog = csv.writer(write, delimiter= '\t', quoting=csv.QUOTE_ALL)
				writelog.writerow( (str(num), visible, naid, id, language, api_url ) )
			write.closed
	
			video = video + 1
		offset = offset + 100
except IndexError:
	pass