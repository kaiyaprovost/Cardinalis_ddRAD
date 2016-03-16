## read in csv
## separate data out into pools





import csv
from itertools import permutations
import math

## read file
poolfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_testCSV.csv")
reader = csv.DictReader(poolfile)

##for row in reader:
##    if row["LATITUDE"] != "" :
##        latStrings.append(row["LATITUDE"])
##        longStrings.append(row["LONGITUDE"])
##        ident.append(row["IDENTIFICATION"])

#poolList = ["P1","P2","P3","P4","P5","P6","P7","P8","P9"]
poolList = ["P1","P2","P3"]

p1 = []
p2 = []
p3 = []

for row in reader:
    if row["POOL"] == "P1":
        p1.append(row)
    elif row["POOL"] == "P2":
        p2.append(row)
    elif row["POOL"] == "P3":
        p3.append(row)

poolfile.close()

permuteList = []

first = True
for i in permutations(poolList,len(poolList)):
    if first == True:
        original = i
        first = False
    permuteList.append(i)

##print first
##print original

def poolSwap(pool1,pool2):
    for j in range(len(pool1)):
        pool1[j],pool2[j] = pool2[j],pool1[j]

for perm in permuteList:
    for m in range(len(perm)):
        if perm != original:
            print perm[m],original[m]

