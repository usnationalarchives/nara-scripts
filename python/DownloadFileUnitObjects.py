import requests, json, time, csv, os, datetime, os.path, urllib.request, sys, glob, img2pdf, PyPDF2
from os import mkdir
from os import path
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader

print(datetime.datetime.now().time())

if not os.path.exists('objects'):
    mkdir('objects')

nextCursorMark = '*'
while nextCursorMark != '':
    try: #replace NAID in the URL below with the NAID of the File Unit (...description.fileUnit.naId=[YOUR NAID]&type...)
        j = json.loads(requests.get('https://catalog.archives.gov/api/v1?description.fileUnit.naId=119624856&type=object&resultFields=parentDescriptionNaId,objects.object.file&rows=1000&cursorMark=' + nextCursorMark).text)
        writeFile = open('downloadObjects.json', 'w')
        json.dump(j, writeFile)
        writeFile.close()

        pathname = 'downloadObjects.json'

        with open(pathname) as f:
            dat = f.read()
            json_data = json.loads(dat)

        for record in j['opaResponse']['results']['result']:
            parentNaId = str(record['parentDescriptionNaId'])
            url = str(record['objects']['object']['file']['@url'])
 


            allItems = (parentNaId, url)
         
                
            with open('ListOfObjectsToDownload.csv','a', encoding='utf-8') as log :
                writelog = csv.writer(log)
                for record in j:
                    writelog.writerow(allItems)


        print(j['opaResponse']['results']['nextCursorMark'])

        nextCursorMark = j['opaResponse']['results']['nextCursorMark']

    except KeyError:
        print('Object list created - all pages complete!')
        break

with open('ListOfObjectsToDownload.csv', 'r') as log:
    readfile = csv.reader(log, delimiter=',')
    for row in readfile:
        parentNaId = row[0]
        link = row[1]

        link = link.strip()
        name = link.rsplit('/')[-1]
        filename = os.path.join('objects', name)

        if not os.path.isfile(filename):
            print('Downloading: ' + filename)
            try:
                urllib.request.urlretrieve(link, filename)
            except Exception as inst:
                print(inst)
f = open('ListOfObjectsToDownload.csv', 'w')
f.write('')
f.close()

print('All JPGs downloaded! ' + str(datetime.datetime.now().time()))

print('Compressing JPGs:')

os.chdir('objects')
if not os.path.exists('Compressed'):
    mkdir('Compressed')

def compressMe(file, verbose=False):
    filepath = os.path.join(os.getcwd(), file)
    oldsize = os.stat(filepath).st_size
    picture = Image.open(filepath)
    dim = picture.size
    
    #set quality= to the preferred quality. 
    #Original script creator found that 85 has no difference in their 6-10mb files and that 65 is the lowest reasonable number
    #I am using 45 and it seems to work...
    picture.save("Compressed/Compressed_"+file,"JPEG",optimize=True,quality=45) 
    
    newsize = os.stat(os.path.join(os.getcwd(),"Compressed/Compressed_"+file)).st_size
    percent = (oldsize-newsize)/float(oldsize)*100
    if (verbose):
        print("File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
    return percent

def main():
    verbose = False
    #checks for verbose flag
    if (len(sys.argv)>1):
        if (sys.argv[1].lower()=="-v"):
            verbose = True

    #finds present working dir
    pwd = os.getcwd()

    tot = 0
    num = 0
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            num += 1
            tot += compressMe(file, verbose)
    print("Average Compression: %d" % (float(tot)/num))
    print("Done")

if __name__ == "__main__":
    main()

print('All done compressing!' + str(datetime.datetime.now().time()))

print('Creating PDFs and combining into one:')

os.chdir('..')

for filename in sorted(glob.glob('objects/Compressed/*.jpg')):

    img_path = filename
    pdf_path = filename[:-4] + '.pdf'

    image = Image.open(img_path)

    pdf_bytes = img2pdf.convert(image.filename)

    file = open(pdf_path, 'wb')

    file.write(pdf_bytes)

    image.close()

    file.close()

print('Successfully created individual pdf files!  ' + str(datetime.datetime.now().time()))


merger = PyPDF2.PdfFileMerger()


for filename in sorted(glob.glob('objects/Compressed/*.pdf')):                               
    input = PyPDF2.PdfFileReader(open(filename,'rb'))
    merger.append((input))

#Replace the filename below with the NAID of the File Unit, or any other name you want to use for the combined PDF.
merger.write('119624856.pdf')
                      

print('Successfully merged pdf files!  ' + str(datetime.datetime.now().time()))


