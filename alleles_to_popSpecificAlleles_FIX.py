def snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList,chiList,outList):
    #print "sonlist1",sonList,"chilist1",chiList
    for k in range(len(tempLocusList)):

        if tempNameList[k] == "Son":
            if tempLocusList[k][j] not in sonList:
                sonList = sonList + str(tempLocusList[k][j])

        elif tempNameList[k] == "Chi":
            if tempLocusList[k][j] not in chiList:
                chiList = chiList + str(tempLocusList[k][j])

        elif tempNameList[k] == "Out":
            if tempLocusList[k][j] not in outList:
                outList = outList + str(tempLocusList[k][j])

    return [sonList,chiList,outList]

def indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent):
    indel = False
    if noIndel == True: ## check if should remove Indels
        for loci in tempLocusList:
            if "-" in loci:
                indel = True ## if indels, flags True
        if indel == False: ## no indels found, print
            print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)+"\t"+str(outList)+"\t"+str(len(popsPresent))
        else: ## indels found, print nothing
            indel = False
    elif noIndel == False:
        print >>cardout, str(locusCount)+"\t"+str(j)+"\t"+str(chiList)+"\t"+str(sonList)+"\t"+str(outList)+"\t"+str(len(popsPresent))
    else:
        print "ERROR - INDEL NOT SPECIFIED"

def addFlagGet(sonList,chiList,outList,popsPresent):
    addFlag = True
    #print "--------------"
    if len(popsPresent) == 3 or popsPresent == ["Son","Chi"]:
        for i in sonList:
            #print sonList,chiList
            for k in chiList:
                #print i,k
                if i == k or sonList in ["N","-","-N","N-"] or chiList in ["N","-","-N","N-"]:
                    addFlag = False
    elif popsPresent == ["Chi","Out"]:
        for i in outList:
            #print outList,chiList
            for k in chiList:
                #print i,k
                if i == k or outList in ["N","-","-N","N-"] or chiList in ["N","-","-N","N-"]:
                    addFlag = False
    elif popsPresent == ["Son","Out"]:
        for i in sonList:
            #print sonList,outList
            for k in outList:
                #print i,k
                if i == k or sonList in ["N","-","-N","N-"] or outList in ["N","-","-N","N-"]:
                    addFlag = False
        
    return addFlag

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
    outList = ""

    popsPresent = []
    
    print "SINGLE SNP: ",singleSNP, 
    print "NO INDEL: ",noIndel
    print "---------------------------------------------------------"
    
    cardout = open(outfile,"w")
    print >>cardout, "LOCUS"+"\t"+"SNP"+"\t"+"CHI"+"\t"+"SON"+"\t"+"OUT"+"\t"+"NUMPOPS"+"\t"+"##SINGLE SNP LOCI ONLY: "+str(singleSNP)+", NO INDEL LOCI ONLY: "+str(noIndel)
    for i in range(len(lines)):
        split = lines[i].split("\t")
        if lines[i][0]== ">": ## sequence
            tempNameList.append(split[0][1:4])
            tempLocusList.append(split[1])
        else: ## locus delimiter
            #print "LOCUS: "+str(locusCount)+"-----------------------------------------------"
            if "Son" in tempNameList:
                popsPresent.append("Son")
            if "Chi" in tempNameList:
                popsPresent.append("Chi")
            if "Out" in tempNameList:
                popsPresent.append("Out")

            if len(popsPresent) >= 2: ## only keep locus if it contains two pops
                lineCheck = split[1]
                lociLength = len(tempLocusList[0])
                ## check through the last line (the // line) to see where the difs are (- and *)
                snpsLoc = [m.start() for m in re.finditer(("\-|\*"),lineCheck)] 

                if singleSNP == True: ## check if should limit to single snp loci
                    if len(snpsLoc) == 1:
                        for j in snpsLoc:
                            bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="",outList="")
                            sonList = bothLists[0]
                            chiList = bothLists[1]
                            outList = bothLists[2]
                            
                            addFlag = addFlagGet(sonList,chiList,outList,popsPresent)
                            if addFlag == True:
                                indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent)
                                sonList = ""
                                chiList = ""
                                outList = ""
                            else:
                                addFlag = True          
                        sonList = ""
                        chiList = ""
                        outList = ""

                elif singleSNP == False:
                    for j in snpsLoc:
                        bothLists = snpFinder2(j,snpsLoc,tempLocusList,tempNameList,sonList="",chiList="",outList="")
                        sonList = bothLists[0]
                        chiList = bothLists[1]
                        outList = bothLists[2]
                        
                        addFlag = addFlagGet(sonList,chiList,outList,popsPresent)
                        if addFlag == True:
                            indelCheck(noIndel,tempLocusList,tempNameList,cardout,locusCount,j,chiList,sonList,outList,popsPresent)
                            sonList = ""
                            chiList = ""
                            outList = ""
                        else:
                            addFlag = True           
                    sonList = ""
                    chiList = ""
                    outList = ""
                else:
                    print "ERROR - SINGLE SNP NOT SPECIFIED"
                    sonList = ""
                    chiList = ""
                    outList = ""
                sonList = ""
                chiList = ""
                outList = ""
            else:
                sonList = ""
                chiList = ""
                outList = ""
            sonList = ""
            chiList = ""
            outList = ""
            popsPresent = []                                                                                     
            tempNameList = []
            tempLocusList = []
            locusCount = locusCount + 1
    cardout.close()

in1  = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeledtabs2.alleles"
out1 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_noMultiSnpLoci_fix.txt"
out2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noIndelLoci_fix.txt"
out3 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_noMultiSnpLoci_fix.txt"
out4 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_list_allBiallelicSnps_fix.txt"

in2 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/testTemp.alleles"
out5 = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/onePop_oneSNP_temp.txt"

singlePopSNP(in1,out1,noIndel=True,singleSNP=True)
singlePopSNP(in1,out2,noIndel=True,singleSNP=False)
singlePopSNP(in1,out3,noIndel=False,singleSNP=True)
singlePopSNP(in1,out4,noIndel=False,singleSNP=False)

singlePopSNP(in2,out5,noIndel=False,singleSNP=False)
