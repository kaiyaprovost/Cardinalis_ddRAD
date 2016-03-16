## program to put a cap of 10 inds per loci
## remove loci with more than 23 inds - have to have more than 10 by def
## all loci already have a minimum of 4 inds

prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.unlinked_snps")
#prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")
lines = prob.readlines()
prob.close()

maxInd = 10
minInd = 4

## open a new file for writing the info out as a .txt
probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_unlinked_locuscap_max"+str(maxInd)+"_min"+str(minInd)+".txt","w")

outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_goodList_max"+str(maxInd)+"_min"+str(minInd)+".txt","w")

## step 1: ID and count the loci with more than 23 individuals
    ## read a line (i)
    ## check the first three characters of the line to determine pop
    ## check which loci have non-N and non-gap
    ## if son > 10 or chi > 10, output it to a "bad list" with number each

names = []
bases = []

for i in range(len(lines)):
    if i != 0:
        splitLines = lines[i].split()
        names.append(splitLines[0])
        bases.append(splitLines[1])

countSon = 0
countChi = 0
bigList = []
goodList = []
smallList = []

for i in range(len(bases[0])): ## goes through all 6750 loci
    for j in range(len(names)): ## goes through each individual
        ## iterate through the loci, then thru individuals
        #print "i=",i,
        #print "j=",j,
        #print names[j][0:3],
        #print bases[j][i],
        if names[j][0:3] == "Chi" and bases[j][i] not in ["N","-"]:
            #print "added Chi",
            countChi = countChi + 1
            #print countChi
        elif names[j][0:3] == "Son" and bases[j][i] not in ["N","-"]:
            countSon = countSon + 1
            #print "added Son",
            #print countSon
        #else:
            #print "not"
    if countChi > maxInd or countSon > maxInd:
        #print "loci too big"
        bigList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)])
    elif countChi < minInd and countSon < minInd:
        smallList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)])
    else:
        #print "loci fine"
        goodList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)])
        
    countSon = 0
    countChi = 0

print "num big loci: ",len(bigList)
print "num small loci: ",len(smallList)
print "num good loci: ",len(goodList)

print >>probout, "## Too big at "+str(maxInd)
for i in bigList:
    print >>probout, i[0],i[1],i[2]

print >>probout, ""
print >>probout, "## Too small at "+str(minInd)
for i in smallList:
    print >>probout, i[0],i[1],i[2]

print >>probout, ""
print >>probout, "## Size fine at "+str(minInd)+"/"+str(maxInd)
for i in goodList:
    print >>probout, i[0],i[1],i[2]

for i in bigList:
    print >>outfile, i[0]

probout.close()
outfile.close()
