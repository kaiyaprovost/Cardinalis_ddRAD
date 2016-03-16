import re

## THIS CODE IS NOT WORKING

maxInd = 10
minInd = 4

goodLoci = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_goodList_max"+str(maxInd)+"_min"+str(minInd)+".txt","r")
good = goodLoci.readlines()
goodLoci.close()

gphocsInfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_klp_convert_labeled3.gphocs","r")
gphocs = gphocsInfile.readlines()
gphocsInfile.close()

outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_klp_convert_labeled3_reduced_max"+str(maxInd)+"_min"+str(minInd)+"TEST.gphocs","w")

locusCount = 0
tempLoci = []
locusGood = False

for i in range(len(good)):
    good[i] = good[i].strip()
    ##print good[i]

print >>outfile, str(len(good))

for i in range(len(gphocs)):
    if "locus" in gphocs[i]:
        split = gphocs[i].split()
        if split[0] in good:
            locusGood = True
            #print "keep it"
            tempLoci.append(gphocs[i].strip())
            #print tempLoci
        else:
            #print "remove it"
            locusGood = False
            for j in tempLoci:
                print >>outfile, j
            tempLoci = []
            #print tempLoci
    else:
        ##print "not locus"
        if locusGood == True:
            tempLoci.append(gphocs[i].strip())
            #print tempLoci
        else:
            tempLoci = []
            #print tempLoci
         
outfile.close()

