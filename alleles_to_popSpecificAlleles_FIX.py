def snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList,chiList,outList):
    '''
    Finds SNPS for a given site J across a locus
    '''
    #print "sonlist1",sonList,"chilist1",chiList
    for k in range(len(tempLocusList)):
        ## for each of the temporary individual genotypes within a single locus
        if tempNameList[k] == "Son":
            ## if the individual is from the sonoran desert
            if tempLocusList[k][j] not in sonList:
                ## and the SNP located at site J is not already in the list of sonoran SNPS
                ## add it
                sonList = sonList + str(tempLocusList[k][j])
        elif tempNameList[k] == "Chi":
            ## iff the individual is from the chihuauhan desert
            if tempLocusList[k][j] not in chiList:
                ## and the SNP located at site J is not already in the list of chihuahuan SNPS
                ## add it
                chiList = chiList + str(tempLocusList[k][j])
        elif tempNameList[k] == "Out":
            ## if the individual is from the outgroup
            if tempLocusList[k][j] not in outList:
                ## and the snp located at site J is not already in the list of outgroup snps
                ## add it
                outList = outList + str(tempLocusList[k][j])
    ## return the complete list of snps in each desert for the locus
    return [sonList,chiList,outList]

def indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent):
    '''
    Checks to see if a locus has indels, and whether or not to exclude that locus from being printed
    '''
    indel = False
    ## set the flag for if the locus contains an indel to false
    if noIndel == True:
        ## if indels need to be removed
        for loci in tempLocusList:
            ## for each individual's genotype in the locus
            if "-" in loci:
                indel = True
                ## if indels, flag that there are indels
        if indel == False:
            ## if no indels found, print out the locus' snps
            print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)+"\t"+str(outList)+"\t"+str(len(popsPresent))
        else:
            ## indels are found, print nothing
            ## reset the indel checker to false
            indel = False
    elif noIndel == False:
        ## if indels do not need to be removed
        ## print all of the locus' snps
        print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)+"\t"+str(outList)+"\t"+str(len(popsPresent))
    else:
        print "ERROR - INDEL NOT SPECIFIED"

def addFlagGet(sonList,chiList,outList,popsPresent):
    '''
    Checks to see whether the locus should be flagged for printing
    '''
    addFlag = True
    ## check for which population types the locus contains
    ## and check to see if the locus contains indels or ambiguities
    ## or if the locus has the same SNP calls for each population
    #print "--------------"
    if len(popsPresent) == 3 or popsPresent == ["Son","Chi"]:
        ## if all three populations are present, or both sonoran and chihuahuan are present
        for i in sonList:
            #print sonList,chiList
            for k in chiList:
                #print i,k
                if i == k or sonList in ["N","-","-N","N-"] or chiList in ["N","-","-N","N-"]:
                    ## if the two are not equal, or one contains only indels/ambiguities
                    ## set the flag to false
                    addFlag = False
    elif popsPresent == ["Chi","Out"]:
        ## if the population has only chihuahuan and outgroup
        for i in outList:
            #print outList,chiList
            for k in chiList:
                #print i,k
                if i == k or outList in ["N","-","-N","N-"] or chiList in ["N","-","-N","N-"]:
                    ## if the two are not equal, or one contains only indels/ambiguities
                    ## set the flag to false
                    addFlag = False
    elif popsPresent == ["Son","Out"]:
        ## if the population has only sonoran and outgroup
        for i in sonList:
            #print sonList,outList
            for k in outList:
                #print i,k
                if i == k or sonList in ["N","-","-N","N-"] or outList in ["N","-","-N","N-"]:
                    ## if the two are not equal, or one contains only indels/ambiguities
                    ## set the flag to false
                    addFlag = False
        
    return addFlag

def singlePopSNP(infile,outfile,noIndel=True,singleSNP=True):
    '''
    Finds all loci that have SNPS that are population-specific
    '''
    import re

    ## open and read the file
    card = open(infile,"r")
    lines = card.readlines()
    card.close()

    ## set up blank lists and counters
    locusCount = 0
    tempLocusList = []
    tempNameList = []
    sonList = ""
    chiList = ""
    outList = ""

    popsPresent = []

    ## states whether only loci with single SNPS or loci without indels should be included
    print "SINGLE SNP: ",singleSNP, 
    print "NO INDEL: ",noIndel
    print "---------------------------------------------------------"

    ## open the file for printing and add a header
    cardout = open(outfile,"w")
    print >>cardout, "LOCUS\tSNP\tCHI\tSON\tOUT\tNUMPOPS\t##SINGLE SNP LOCI ONLY: "+str(singleSNP)+", NO INDEL LOCI ONLY: "+str(noIndel)

    ## for each line in the loci file
    for i in range(len(lines)):
        ## split the lines into names and into sequences
        split = lines[i].split("\t")
        if lines[i][0]== ">": ## if the line is a data line, not a locus delimiter
            ## add the name and the locus to the temporary storage lists for names and loci
            tempNameList.append(split[0][1:4])
            tempLocusList.append(split[1])
        else: ## if the line is a locus delimiter
            #print "LOCUS: "+str(locusCount)+"-----------------------------------------------"
            ## check to see which populations are present in the locus
            if "Son" in tempNameList:
                popsPresent.append("Son")
            if "Chi" in tempNameList:
                popsPresent.append("Chi")
            if "Out" in tempNameList:
                popsPresent.append("Out")

            if len(popsPresent) >= 2: ## only keep locus if it contains two pops
                
                ## get the SNP information of the locus delimiter, and the length of the locus
                lineCheck = split[1]
                lociLength = len(tempLocusList[0])

                ## check through the last line (the // line) to see where the SNPS are (- and *)
                snpsLoc = [m.start() for m in re.finditer(("\-|\*"),lineCheck)] 

                ## check if should limit to single snp loci or not
                if singleSNP == True: 
                    ## if yes
                    if len(snpsLoc) == 1:
                        ## if only one SNP is found, keep the locus
                        
                        for j in snpsLoc:
                            ## for each SNP, get the population level variation and save it
                            bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="",outList="")
                            sonList = bothLists[0]
                            chiList = bothLists[1]
                            outList = bothLists[2]

                            ## check to see if the locus should be kept
                            addFlag = addFlagGet(sonList,chiList,outList,popsPresent)
                            if addFlag == True:
                                ## if the locus should be kept, check to see if it contains indels and print it
                                indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent)
                                ## reset the lists
                                sonList = ""
                                chiList = ""
                                outList = ""
                            else:
                                ## if the locus should not be kept, reset the addFlag flag
                                addFlag = True          
                        ## reset the lists
                        sonList = ""
                        chiList = ""
                        outList = ""

                ## if should not limit to single SNP loci
                elif singleSNP == False:
                    for j in snpsLoc:
                        ## for each SNP, get the population level variation and save it
                        bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="",outList="")
                        sonList = bothLists[0]
                        chiList = bothLists[1]
                        outList = bothLists[2]

                        ## check to see if the locus should be kept
                        addFlag = addFlagGet(sonList,chiList,outList,popsPresent)
                        if addFlag == True:
                            ## if the locus should be kept, check to see if it contains indels and print it
                            indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent)
                            ## reset the lists
                            sonList = ""
                            chiList = ""
                            outList = ""
                        else:
                            ## if the locus should not be kept, reset the addFlag flag
                            addFlag = True           
                    ## reset the lists
                    sonList = ""
                    chiList = ""
                    outList = ""
                else:
                    ## if the singleSNP argument is not set, throw an error and reset the lists
                    print "ERROR - SINGLE SNP NOT SPECIFIED"
                    sonList = ""
                    chiList = ""
                    outList = ""
                ## reset the list
                sonList = ""
                chiList = ""
                outList = ""
            else: ## if the locus does not contain at least two populations, reset the lists
                sonList = ""
                chiList = ""
                outList = ""
            ## and reset the lists and the counters
            sonList = ""
            chiList = ""
            outList = ""
            popsPresent = []                                                                                     
            tempNameList = []
            tempLocusList = []
            locusCount = locusCount + 1
    cardout.close()

if __name__ == "__main__":
    

    ## input an alleles infile and set up outfiles
    in1  = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeledtabs2.alleles"
    out1 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci_fix.txt"
    out2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_fix.txt"
    out3 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci_fix.txt"
    out4 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps_fix.txt"

    in2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/testTemp.alleles"
    out5 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_temp.txt"

    ## run the functions
    singlePopSNP(in1,out1,noIndel=True,singleSNP=True)
    singlePopSNP(in1,out2,noIndel=True,singleSNP=False)
    singlePopSNP(in1,out3,noIndel=False,singleSNP=True)
    singlePopSNP(in1,out4,noIndel=False,singleSNP=False)

    singlePopSNP(in2,out5,noIndel=False,singleSNP=False)
