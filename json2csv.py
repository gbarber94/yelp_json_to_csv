"""
Gregory Barber
12/12/2018
Converting Yelp Json Data to csv

"""
import csv
import re

row = []
cat = []
catb = False
csvout = open('testjson2csv.csv', 'w')
recordwriter = csv.writer(csvout, dialect='unix', quoting=csv.QUOTE_MINIMAL)

#header csv
header = ['name','address','city','state','latitude','longitude','stars','review_count',"categories"]
recordwriter.writerow([s.encode('utf8') for s in header])

def column_selector(i,catb,cat,start,end):
    for j in i:
        if j.startswith(start) == True:
            catb = True
        if catb == True and j.startswith(end) == False:
            j = re.sub('(.*:)',"",j)
            cat.append(j)
        if j.startswith(end) == True:
            #print(cat)
            cat = ''.join(cat)
            row.append(cat)
            catb = False
    return row

with open('business.json',encoding='utf8') as csvfile:
    recordreader = csv.reader(csvfile)
    #print(recordreader)
    for i in recordreader:
        column_selector(i,catb,[],'name','neighborhood')
        column_selector(i,catb,[],'address:','city')
        column_selector(i,catb,[],'city:','state')
        column_selector(i,catb,[],'state:','postal_code')
        column_selector(i,catb,[],'latitude:','longitude')
        column_selector(i,catb,[],'longitude:','stars')
        column_selector(i,catb,[],'stars','review_count')
        column_selector(i,catb,[],'review_count','is_open')
        column_selector(i,catb,[],'categories:','hours')

        #print(row)
        recordwriter.writerow([s.encode('utf8') for s in row])
        row = []
        #x += 1
        #if x == 1:
        #    break
