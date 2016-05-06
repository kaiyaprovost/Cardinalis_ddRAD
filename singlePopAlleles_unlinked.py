def compareAlleles(sonList,chiList,outList,filename):
    sumJ = 0
    sumK = 0
    sumM = 0
    print >>filename, "POP","\t","LOCUS","\t","ALLELE" ## print a header
    lenSon = len(sonList) ## the length of each population to iterate over
    lenChi = len(chiList)
    lenOut = len(outList)
    if lenSon != lenOut or lenChi != lenOut or lenSon != lenChi: ## check lists are the same length
        return "Error! Lists must be same length of loci"
    else:
        locusLen = lenSon
    for locus in range(locusLen): ## for each individual locus
            for j in sonList[locus]: ## for each sonoran snp found at the locus 
                if j not in chiList[locus] and j not in outList[locus]:
                    ## the snp, j, is unique allele
                    print >>filename, "son"+"\t"+"locus"+str(locus)+"\t"+str(j) ## print the desert, locus number, and snp to a file
                
                sumJ = len(j) + sumJ ## add the locus to the list of loci found 
            for k in chiList[locus]: ## repeat protocol for chihuahuan snps
                if k not in sonList[locus] and k not in outList[locus]:
                    ## k is unique allele
                    print >>filename, "chi"+"\t"+"locus"+str(locus)+"\t"+str(k)
                sumK = len(k) + sumK
            for m in outList[locus]: ## repeat protocol for outgroup snps
                if m not in sonList[locus] and m not in chiList[locus]:
                    print >>filename, "out"+"\t"+"locus"+str(locus)+"\t"+str(m)
                sumM = len(m) + sumM 
    print "son alleles","chi alleles","out alleles"
    print sumJ,sumK,sumM
    return sumJ,sumK,sumM

if __name__ == "__main__":

    ## read in the file and read in the lines to iterate over
    ## these lines are the snp calls for each individual for each locus
    prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.unlinked_snps")
    #prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")
    lines = prob.readlines()
    prob.close()

    ## open a new file for writing the info out as a .txt
    probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_allele_information.txt","w")
    #probout = open("C:/Users/Kaiya/Desktop/allelocitestoutput.txt","w")

    ## steps:
        ## read a line (i)
        ## check the first 3 characters of the line to get the population
        ## read the Nth character in the line - that is the locus
    ## go to that locus (j) within a population list
        ## if the Nth character is not already associated with that pop, add it to the pop for that locus
        ## if the Nth character is already associated, do nothing

    ## initialize line and locus counters, and whether or not the item is the first of its desert
    countLine = 0
    countLoci = 0
    firstSon = 0
    firstChi = 0
    firstOut = 0

    ## initialize empty lists the length of the locus
    ## each of these lists will be populated with ALL bases at a locus for a given population
    sonList = [None] * len(lines[1].split()[1])
    chiList = [None] * len(lines[1].split()[1])
    outList = [None] * len(lines[1].split()[1])

    for i in range(len(lines)):
        if countLine != 0: ## if the line is not the first line (header)
            splitLines = lines[i].split()
            #print splitLines
            if splitLines[0][0:3] == "Son": ## if the sample is from the sonoran desert
                for j in range(len(splitLines[1])): ## for each base pair
                    if splitLines[1][j] in ["Y","R","K","W","S","M"]: ## if the base is ambiguous
                        diploid = True ## the organism is diploid at the base
                    else: ## if the base is not ambiguous
                        diploid = False ## the organism is not diploid at the base
                    x = sonList[j] ## extract all the bases found at this part of the locus
                    if x == None: ## if there are no bases found yet
                        x = "" ## set the master list to blank
                    if diploid == False: ## if there is only one base at this locus
                        if splitLines[1][j] not in x: ## if the current base is not in the list of bases found
                            x = str(x)+str(splitLines[1][j]) ## add it
                    if diploid == True: ## if there is more than one base
                        ## disambiguate the bases and add the component bases
                        if splitLines[1][j] == "Y": 
                            if "C" not in x:
                                x = str(x)+"C"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "R":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "K":
                            if "G" not in x:
                                x = str(x)+"G"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "W":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "S":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "M":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "A" not in x:
                                x = str(x)+"A"
                    sonList[j] = x ## update the list of found snps to include the current locus
                    ## this protocol gets repeated for each desert

            if splitLines[0][0:3] == "Chi": ## if the desert is the chihuahuan, repeat above
                for j in range(len(splitLines[1])):
                    if splitLines[1][j] in ["Y","R","K","W","S","M"]:
                        diploid = True
                    else:
                        diploid = False
                    x = chiList[j]
                    if x == None:
                        x = ""
                    if diploid == False:
                        if splitLines[1][j] not in x:
                            x = str(x)+str(splitLines[1][j])
                    if diploid == True:
                        if splitLines[1][j] == "Y":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "R":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "K":
                            if "G" not in x:
                                x = str(x)+"G"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "W":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "S":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "M":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "A" not in x:
                                x = str(x)+"A"
                    chiList[j] = x

            if splitLines[0][0:3] == "Out": ## if the desert is the chihuahuan, repeat above
                for j in range(len(splitLines[1])):
                    if splitLines[1][j] in ["Y","R","K","W","S","M"]:
                        diploid = True
                    else:
                        diploid = False
                    x = outList[j]
                    if x == None:
                        x = ""
                    if diploid == False:
                        if splitLines[1][j] not in x:
                            x = str(x)+str(splitLines[1][j])
                    if diploid == True:
                        if splitLines[1][j] == "Y":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "R":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "K":
                            if "G" not in x:
                                x = str(x)+"G"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "W":
                            if "A" not in x:
                                x = str(x)+"A"
                            if "T" not in x:
                                x = str(x)+"T"
                        if splitLines[1][j] == "S":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "G" not in x:
                                x = str(x)+"G"
                        if splitLines[1][j] == "M":
                            if "C" not in x:
                                x = str(x)+"C"
                            if "A" not in x:
                                x = str(x)+"A"
                    outList[j] = x
        else: ## if the line is the first line
            splitLines = "" ## reset the splitLine to the empty list
        countLine = countLine + 1 ## move to the next individual's line

               
    compareAlleles(sonList,chiList,outList,probout)

    ## close the new file
    probout.close()
