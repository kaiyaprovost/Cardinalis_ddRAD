## program to put a cap of 10 inds per loci
## remove loci with more than 23 inds - have to have more than 10 by def
## all loci already have a minimum of 4 inds

import re

#prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_klp_convert_labeled3.gphocs")
prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")
lines = prob.readlines()
prob.close()

maxInd = 8
minInd = 5

## open a new file for writing the info out as a .txt
#probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+".gphocs","w")

probout = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","w")

#outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_goodList_max"+str(maxInd)+"_min"+str(minInd)+".txt","w")

## step 1: ID and count the loci with more than 23 individuals
    ## read a line (i)
    ## check the first three characters of the line to determine pop
    ## check which loci have non-N and non-gap
    ## if son > 10 or chi > 10, output it to a "bad list" with number each

tempLoci = []
firstLoci = True

countSon = 0
countChi = 0

print >>probout, "NUMLOCI"

for i in range(len(lines)):
    if "locus" in lines[i]:
        if firstLoci == True:
            firstLoci = False
            tempLoci.append(lines[i])
            #print tempLoci
        else:
            for j in range(len(tempLoci)):
                if tempLoci[j][0:3] == "Son":
                    countSon = countSon + 1
                if tempLoci[j][0:3] == "Chi":
                    countChi = countChi + 1
            #print countSon,countChi
            if countSon <= maxInd and countChi <= maxInd:
                #print "less",
                if countSon > minInd and countChi > minInd:
                    #print "more"
                    for k in tempLoci:
                        print >>probout, k,
                else:
                    #print "not"
                    x = 0
                tempLoci = []
            else:
                #print "not"
                tempLoci = []
            countSon = 0
            countChi = 0
            tempLoci.append(lines[i])
            #print tempLoci
    else:
        tempLoci.append(lines[i])
        #print tempLoci

probout.close()

#replace = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+".gphocs","r")
replace = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","r")
read = replace.read()
replace.close()

print read

count = read.count("locus")
#print count
temp = re.sub("NUMLOCI",str(count),read)
print temp[0:50]

#replace = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+".gphocs","w")
replace = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","w")
print >>replace, temp
replace.close()


#outfile.close()
