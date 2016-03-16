allSnpsString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps.txt"
noMultiString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci.txt"
noInMulString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci.txt"
noIndelString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci.txt"

allSnpsFile = open(allSnpsString,"r")
noMultiFile = open(noMultiString,"r")
noInMulFile = open(noInMulString,"r")
noIndelFile = open(noIndelString,"r")

allSnps = allSnpsFile.readlines()
noMulti = noMultiFile.readlines()
noInMul = noInMulFile.readlines()
noIndel = noIndelFile.readlines()

allSnpsFile.close()
noMultiFile.close()
noInMulFile.close()
noIndelFile.close()

def extractGoodSnps(lines,listOfHeaderLines):
    goodLoci = []
    for i in range(len(lines)):
        if i not in listOfHeaderLines:
            splitLines = lines[i].split()
            goodLoci.append(int(splitLines[0]))
    goodLoci = list(set(goodLoci))
    goodLoci.sort()
    return goodLoci

allSnpsList = extractGoodSnps(allSnps,[0,1])
noMultiList = extractGoodSnps(noMulti,[0,1])
noInMulList = extractGoodSnps(noInMul,[0,1])
noIndelList = extractGoodSnps(noIndel,[0,1])

def extractLoci(lociFileLines,listOfLoci,outfile):
    locusCount = 0
    for i in range(len(lociFileLines)):
        if locusCount in listOfLoci:
            #print locusCount
            #print lociFileLines[i]
            print >>outfile, lociFileLines[i],
        splitLines = lociFileLines[i].split()
        if splitLines[0][0:2] == "//":
            locusCount = locusCount + 1

lociFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci","r")
lociFileLines = lociFile.readlines()
lociFile.close()

allSnpsOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_allBiallelicSnps.loci","w")
noMultiOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noMultiSnpLoci.loci","w")
noInMulOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_noMultiSnpLoci.loci","w")
noIndelOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci.loci","w")

extractLoci(lociFileLines,allSnpsList,allSnpsOut)
extractLoci(lociFileLines,noMultiList,noMultiOut)
extractLoci(lociFileLines,noInMulList,noInMulOut)
extractLoci(lociFileLines,noIndelList,noIndelOut)

allSnpsOut.close()
noMultiOut.close()
noInMulOut.close()
noIndelOut.close()
