import csv, glob

for filename in sorted(glob.glob("metadata/*.csv")):
        file_a = filename[:-4]
        file = file_a[9:]

        csvFile = 'metadata/' + file + '.csv'
        xmlFile = file + '.xml'

        csvData = csv.reader(open(csvFile, encoding='latin-1'))
        xmlData = open(xmlFile, 'w', encoding='latin-1')
        xmlData.write('<?xml version="1.0"?>' + "\n")

        xmlData.write('<root>' + "\n")

        rowNum = 0
        for row in csvData:
                if rowNum == 0:
                        tags = row

                        for i in range(len(tags)):
                                tags[i].replace(' ', '_')
                else:
                        xmlData.write('<row>' + "\n")
                        for i in range(len(tags)):
                                xmlData.write('     ' + '<' + tags[i] + '>'\
                                              + row[i] + '</' + tags[i] + '>' + "\n")
                        xmlData.write('</row>' + "\n")
                rowNum +=1
        xmlData.write('</root>' + "\n")
        xmlData.close()