allSnpsString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps_fix.txt"
noMultiString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci_fix.txt"
noInMulString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci_fix.txt"
noIndelString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_fix.txt"

allSnpsFile = open(allSnpsString,"rU")
noMultiFile = open(noMultiString,"rU")
noInMulFile = open(noInMulString,"rU")
noIndelFile = open(noIndelString,"rU")

allSnps = allSnpsFile.readlines()
noMulti = noMultiFile.readlines()
noInMul = noInMulFile.readlines()
noIndel = noIndelFile.readlines()

allSnpsFile.close()
noMultiFile.close()
noInMulFile.close()
noIndelFile.close()

def extractGoodSnps(lines,listOfHeaderLines,minPops):
    goodLoci = []
    for i in range(len(lines)):
        if i not in listOfHeaderLines:
            splitLines = lines[i].split("\t")
            nums = int(splitLines[5].strip())
            if nums >= minPops: ## needs to meet min number of pops
                goodLoci.append(int(splitLines[0]))
    goodLoci = list(set(goodLoci))
    goodLoci.sort()
    return goodLoci

allSnpsList = extractGoodSnps(allSnps,[0],3)
noMultiList = extractGoodSnps(noMulti,[0],2)
noInMulList = extractGoodSnps(noInMul,[0],2)
noIndelList = extractGoodSnps(noIndel,[0],3)

def extractLoci(lociFileLines,listOfLoci,outfile):
    locusCount = 0
    for i in range(len(lociFileLines)):
        if locusCount in listOfLoci:
            print >>outfile, str(lociFileLines[i].strip())+"\tLOCUS: "+str(locusCount)
        splitLines = lociFileLines[i].split()
        if splitLines[0][0:2] == "//":
            locusCount = locusCount + 1
                  
lociFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci","r")
lociFileLines = lociFile.readlines()
lociFile.close()

allSnpsOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_allBiallelicSnps_fix.loci","w")
noMultiOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noMultiSnpLoci_fix.loci","w")
noInMulOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_noMultiSnpLoci_fix.loci","w")
noIndelOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_fix.loci","w")

extractLoci(lociFileLines,allSnpsList,allSnpsOut)
extractLoci(lociFileLines,noMultiList,noMultiOut)
extractLoci(lociFileLines,noInMulList,noInMulOut)
extractLoci(lociFileLines,noIndelList,noIndelOut)

allSnpsOut.close()
noMultiOut.close()
noInMulOut.close()
noIndelOut.close()
