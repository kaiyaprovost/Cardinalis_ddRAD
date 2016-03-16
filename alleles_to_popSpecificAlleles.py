def snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList,chiList):
    #print "sonlist1",sonList,"chilist1",chiList
    for k in range(len(tempLocusList)):
        #print "j=",j,"k=",k,
##        print "locusList","name=",tempNameList[k],"snp=",tempLocusList[k][j]
##        if  tempLocusList[k][j] == "N":
##            print "LOCUS IS N"
        if tempNameList[k] == "Son":
            if tempLocusList[k][j] not in sonList and tempLocusList[k][j] != "N":
                #print "before Son",sonList,
                sonList = sonList + str(tempLocusList[k][j])
                #print "after Son",sonList
        elif tempNameList[k] == "Chi":
            if tempLocusList[k][j] not in chiList and tempLocusList[k][j] != "N":
                #print "before Chi",chiList,
                chiList = chiList + str(tempLocusList[k][j])
                #print "after Chi",chiList
##    print "sonlist2",sonList,"chilist2",chiList
    #print "END LOOP"
    return [sonList,chiList]

def indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList):
    indel = False
    if noIndel == True: ## check if should remove Indels
        #print "NOINDEL = TRUE"
        for loci in tempLocusList:
            if "-" in loci:
                indel = True ## if indels, flags True
        if indel == False: ## no indels found, print
            print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)
            #print str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)
        else: ## indels found, print nothing
            indel = False
            #print "INDELS = BAD"
    elif noIndel == False:
        #print "NOINDEL = FALSE"
        print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)
        #print str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)
    else:
        print "ERROR - INDEL NOT SPECIFIED"

def singlePopSNP(infile,outfile,noIndel=True,singleSNP=True):
    import re
    card = open(infile,"r")
    lines = card.readlines()
    card.close()
    locusCount = 0
    tempLocusList = []
    tempNameList = []
    sonList = ""
    chiList = ""
    print "SINGLE SNP: ",singleSNP, 
    print "NO INDEL: ",noIndel
    print "---------------------------------------------------------"
    cardout = open(outfile,"w")
    print >>cardout, "##SINGLE SNP LOCI ONLY: "+str(singleSNP)+", NO INDEL LOCI ONLY: "+str(noIndel)
    print >>cardout, "LOCUS"+"\t"+"SNP"+"\t"+"CHI"+"\t"+"SON"
    for i in range(len(lines)):
        split = lines[i].split("\t")
        if lines[i][0]== ">": ## sequence
            tempNameList.append(split[0][1:4])
            tempLocusList.append(split[1])
        else: ## locus delimiter
            #print "LOCUS: "+str(locusCount)+"-----------------------------------------------"
            if "Son" in tempNameList and "Chi" in tempNameList: ## only keep locus if it contains both pops
                #print "BOTH POPS"
                lineCheck = split[1]
                lociLength = len(tempLocusList[0])
                snpsLoc = [m.start() for m in re.finditer(("\-|\*"),lineCheck)] ## check through the last line (the // line) to see where the difs are (- and *)
                if singleSNP == True: ## check if should limit to single snp loci
                    #print "SINGLE SNP TRUE"
                    if len(snpsLoc) == 1:
                        for j in snpsLoc:
                            bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="")
                            sonList = bothLists[0]
                            chiList = bothLists[1]
                            #print sonList,chiList,j
                            if len(sonList) == 1 and len(chiList) == 1 and sonList != chiList:
                                indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList)
                                sonList = ""
                                chiList = ""
                    sonList = ""
                    chiList = ""
                elif singleSNP == False:
                    #print "SINGLE SNP FALSE"
                    for j in snpsLoc:
                        bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="")
                        sonList = bothLists[0]
                        chiList = bothLists[1]
                        #print sonList,chiList,j
                        if len(sonList) == 1 and len(chiList) == 1 and sonList != chiList:
                            indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList)
                            sonList = ""
                            chiList = ""
                    sonList = ""
                    chiList = ""
                else:
                    print "ERROR - SINGLE SNP NOT SPECIFIED"
                    sonList = ""
                    chiList = ""
                sonList = ""
                chiList = ""
            else:
                #print "ONE POP END",tempNameList
                sonList = ""
                chiList = ""
            sonList = ""
            chiList = ""
            tempNameList = []
            tempLocusList = []
            locusCount = locusCount + 1
            #print "ROUND END"
    cardout.close()


in1  = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeledtabs2.alleles"
out1 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci.txt"
out2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci.txt"
out3 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci.txt"
out4 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps.txt"

in2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/testTemp.alleles"
out5 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_temp.txt"

singlePopSNP(in1,out1,noIndel=True,singleSNP=True)
singlePopSNP(in1,out2,noIndel=True,singleSNP=False)
singlePopSNP(in1,out3,noIndel=False,singleSNP=True)
singlePopSNP(in1,out4,noIndel=False,singleSNP=False)

singlePopSNP(in2,out5,noIndel=True,singleSNP=False)
