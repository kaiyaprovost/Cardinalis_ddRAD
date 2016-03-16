## NOT WORKING/NOT DONE


allSnpsFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_allBiallelicSnps_fix_ONLYALLPOPS_tabbed.loci","rU")
noIndelFile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_onePoponeSNP_noIndelLoci_fix_ONLYALLPOPS_tabbed.loci","rU")

allSnps = allSnpsFile.readlines()
noIndel = noIndelFile.readlines()

allSnpsFile.close()
noIndelFile.close()

def consensusDNA(lines):

    fullCons = ""
##    sonCons = ""
##    chiCons = ""
##    outCons = ""

    locusCount = 0
    baseCount
    
##
    fullTemp = []
##    sonTemp = []
##    chiTemp = []
##    outTemp = []
##
##    fullLocus = []
##    sonLocus = []
##    chiLocus = []
##    outLocus = []

    for i in range(len(lines)):
        splitLines = lines[i].split("\t")
        if splitLines[0][0] == ">": ## if line is data
            fullLocus.append(splitLines[1].strip())
        else:
            for j in range(len(fullLocus)):
                fullTemp.append(fullLocus[j][baseCount])
            for w in fullTemp:
                
                
                    
            locusCount += 1
    
##    for i in range(len(lines)):
##        splitLines = lines[i].split("\t")
##        if splitLines[0][0] == ">": ## if line is data
##            splitLines[1] = splitLines[1].strip()
##            fullTemp = [""] * len(splitLines[1])
##            for j in range(len(splitLines[1])):
##                if splitLines[1][j] not in fullTemp[j]:
##                    fullTemp[j]= fullTemp[j] + splitLines[1][j]
##                if splitLines[0][1:4] == "Son":
##                    sonTemp = [""] * len(splitLines[1])
##                    if splitLines[1][j] not in sonTemp[j]:
##                        sonTemp[j]= sonTemp[j] + splitLines[1][j]
##                if splitLines[0][1:4] == "Chi":
##                    chiTemp = [""] * len(splitLines[1])
##                    if splitLines[1][j] not in chiTemp[j]:
##                        chiTemp[j]= chiTemp[j] + splitLines[1][j]
##                if splitLines[0][1:4] == "Out":
##                    outTemp = [""] * len(splitLines[1])
##                    if splitLines[1][j] not in outTemp[j]:
##                        outTemp[j]= outTemp[j] + splitLines[1][j]
##            fullLocus = fullLocus + fullTemp
##            sonLocus = sonLocus + sonTemp
##            chiLocus = chiLocus + chiTemp
##            outLocus = outLocus + outTemp
##        else:
##            for k in range(len(fullLocus)):
##                length = len(fullLocus[k])
##                for w in length:
                    
            



    
test = consensusDNA(noIndel)

def ambigExp(base):
    ## stuff to make an ambig into all the letters - check other file
    if base == "Y":
        expand = "CT"
    elif base == "R":
        expand = "AG"
    elif base == "W":
        expand = "AT"
    elif base == "S":
        expand = "GC"
    elif base == "K":
        expand = "TG"
    elif base == "M":
        expand = "CA"
    else:
        expand = base
    return expand

def ambigSimp(dataList):
    if "A" in dataList:
        hasA = True
    else:
        hasA = False
    if "C" in dataList:
        hasC = True
    else:
        hasC = False
    if "G" in dataList:
        hasG = True
    else:
        hasG = False
    if "T" in dataList:
        hasT = True
    else:
        hasT = False
    if hasA:
        if hasG:
            if hasC:
                if hasT:
                    simp = "N"
                else:
                    simp = "V"
            else:
                if hasT:
                    simp = "D"
                else:
                    simp = "R"
        else:
            if hasC:
                if hasT:
                    simp = "H"
                else:
                    simp = "M"
            else:
                if hasT:
                    simp = "W"
                else:
                    simp = "A"
    else:
        if hasG:
            if hasC:
                if hasT:
                    simp = "B"
                else:
                    simp = "S"
            else:
                if hasT:
                    simp = "K"
                else:
                    simp = "G"
        else:
            if hasC:
                if hasT:
                    simp = "Y"
                else:
                    simp = "C"
            else:
                if hasT:
                    simp = "T"
                else:
                    simp = dataList
    return simp
                    
    
        

    
    
    
    
    

    
    




                        
