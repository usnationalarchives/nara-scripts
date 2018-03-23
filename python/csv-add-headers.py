import csv, glob

for filename in sorted(glob.glob("metadata/*.csv")):
        file_a = filename[:-4]
        file = file_a[9:]
        with open('metadata/' + file + '.csv',newline='', encoding='latin-1') as f:
                    r = csv.reader(f)
                    data = [line for line in r]
        with open('metadata/' + file + '.csv','w',newline='', encoding='latin-1') as f:
                    w = csv.writer(f)
                    w.writerow(['file_name','stableURL','state','county','office','appointment_day','appointment_month','appointment_year','roll'])
                    w.writerows(data)               
                
