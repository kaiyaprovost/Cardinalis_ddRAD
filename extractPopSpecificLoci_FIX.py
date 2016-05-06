def extractGoodSnps(lines,listOfHeaderLines,minPops):
    '''
    read the lines and extract loci that have population-specific snps
    '''
    goodLoci = []
    for i in range(len(lines)):
        if i not in listOfHeaderLines: ## if the line is not a header
            splitLines = lines[i].split("\t") ## split it
            nums = int(splitLines[5].strip()) ## read the population-level column
            if nums >= minPops: ## if the population meets the minimum population number
                goodLoci.append(int(splitLines[0])) ## add the locus to a list of "good" loci
    goodLoci = list(set(goodLoci)) ## return unique values of good loci
    goodLoci.sort() ## sort the good loci
    return goodLoci

def extractLoci(lociFileLines,listOfLoci,outfile):
    '''
    Extract out the base pairs for good loci
    '''
    locusCount = 0
    for i in range(len(lociFileLines)):
        if locusCount in listOfLoci: ## if the current locus is in the good loci list
            print >>outfile, str(lociFileLines[i].strip())+"\tLOCUS: "+str(locusCount) ## print the line to the outfile
        splitLines = lociFileLines[i].split() ## split the line
        if splitLines[0][0:2] == "//": ## if the first two characters of the line are a locus delimiter
            locusCount = locusCount + 1 ## move to next locus

if __name__ == "__main__":

    ## get the filenames for each population sort
    allSnpsString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps_fix.txt"
    noMultiString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci_fix.txt"
    noInMulString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci_fix.txt"
    noIndelString = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_fix.txt"

    ## read the files
    allSnpsFile = open(allSnpsString,"rU")
    noMultiFile = open(noMultiString,"rU")
    noInMulFile = open(noInMulString,"rU")
    noIndelFile = open(noIndelString,"rU")

    ## read the lines
    allSnps = allSnpsFile.readlines()
    noMulti = noMultiFile.readlines()
    noInMul = noInMulFile.readlines()
    noIndel = noIndelFile.readlines()

    ## close the files
    allSnpsFile.close()
    noMultiFile.close()
    noInMulFile.close()
    noIndelFile.close()

    ## read the lines and extract loci that have population-specific snps


    ## extract the good snps
    #allSnpsList = extractGoodSnps(allSnps,[0],3)
    #noMultiList = extractGoodSnps(noMulti,[0],2)
    #noInMulList = extractGoodSnps(noInMul,[0],2)
    #noIndelList = extractGoodSnps(noIndel,[0],3)
    noIndelList2 = extractGoodSnps(noIndel,[0],2)

    ## extract out the base pairs for the good loci
                      
    ## initialize infiles
    #lociFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci","r")
    lociFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_SPLIT.loci","r")
    lociFileLines = lociFile.readlines()
    lociFile.close()

    ## initialize outfiles
    #allSnpsOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_allBiallelicSnps_fix.loci","w")
    #noMultiOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noMultiSnpLoci_fix.loci","w")
    #noInMulOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_noMultiSnpLoci_fix.loci","w")
    #noIndelOut = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_fix.loci","w")
    #noIndelOut2 = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_TWOPOPMIN.loci","w")
    noIndelOut2 = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_TWOPOPMIN_SPLIT.loci","w")

    ## extract the loci
    #extractLoci(lociFileLines,allSnpsList,allSnpsOut)
    #extractLoci(lociFileLines,noMultiList,noMultiOut)
    #extractLoci(lociFileLines,noInMulList,noInMulOut)
    extractLoci(lociFileLines,noIndelList2,noIndelOut2)

    ## close files
    #allSnpsOut.close()
    #noMultiOut.close()
    #noInMulOut.close()
    #noIndelOut.close()
    noIndelOut2.close()
