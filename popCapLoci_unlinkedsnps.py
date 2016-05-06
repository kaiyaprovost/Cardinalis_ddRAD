if __name__ == "__main__":
        

    ## program to put a cap of 10 inds per loci per desert
    ## remove loci with more than 23 inds - have to have more than 10 by def
    ## all loci already have a minimum of 4 inds

    ## open file
    prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.unlinked_snps")
    #prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")
    lines = prob.readlines()
    prob.close()

    ## set maximum and minimum individuals allowed per locus per population
    maxInd = 10
    minInd = 4

    ## open a new file for writing the info out as a .txt
    ## file for the loci themselves
    probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_unlinked_locuscap_max"+str(maxInd)+"_min"+str(minInd)+".txt","w")
    ## file for the list of the loci
    outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_unlinked_goodList_max"+str(maxInd)+"_min"+str(minInd)+".txt","w")

    ## ID and count the loci with more than 23 individuals
        ## read a line (i)
        ## check the first three characters of the line to determine pop
        ## check which loci have non-N and non-gap
        ## if son > 10 or chi > 10, output it to a "bad list" with number each

    names = []
    bases = []

    for i in range(len(lines)): ## for each line of code
        if i != 0: ## if the line is not the first line (Header)
            splitLines = lines[i].split() 
            names.append(splitLines[0]) ## add it to the list of names
            bases.append(splitLines[1]) ## add it to the list of bases

    ## initialize lists and counts
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
            if names[j][0:3] == "Chi" and bases[j][i] not in ["N","-"]: ## if the individual is from the chihuahuan desert and the base in question is not an N or a gap
                #print "added Chi",
                countChi = countChi + 1
                #print countChi
            elif names[j][0:3] == "Son" and bases[j][i] not in ["N","-"]:
                countSon = countSon + 1
                #print "added Son",
                #print countSon
            #else:
                #print "not"
        if countChi > maxInd or countSon > maxInd: ## if either are over the maximum
            #print "loci too big"
            bigList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)]) ## add the locus to the biglist
        elif countChi < minInd or countSon < minInd: ## if either are under the minimum
            smallList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)]) ## add the locus to the small list
        else:
            #print "loci fine"
            goodList.append(["locus"+str(i),"chi:"+str(countChi),"son:"+str(countSon)])
        ## restart and move to next locus    
        countSon = 0
        countChi = 0

    print "num big loci: ",len(bigList)
    print "num small loci: ",len(smallList)
    print "num good loci: ",len(goodList)

    ## print to the list file which ones are too big
    print >>probout, "## Too big at "+str(maxInd)
    for i in bigList:
        print >>probout, i[0],i[1],i[2]

    ## print to the list file which ones are too small
    print >>probout, ""
    print >>probout, "## Too small at "+str(minInd)
    for i in smallList:
        print >>probout, i[0],i[1],i[2]

    ## print to the list file which ones are the right size
    print >>probout, ""
    print >>probout, "## Size fine at "+str(minInd)+"/"+str(maxInd)
    for i in goodList:
        print >>probout, i[0],i[1],i[2]
            print >>outfile, i[0]
        
    ## close files
    probout.close()
    outfile.close()
