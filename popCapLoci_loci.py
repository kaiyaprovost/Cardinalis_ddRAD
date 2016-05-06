if __name__ == "__main__":
    '''
    This code outputs a reduced subset of gphocs loci if you DO NOT have a list of the loci you want
    If you ALREADY have this list, use sizeRangeLociOnly.py instead
    '''
        
    ## program to put a cap of 10 inds per loci
    ## remove loci with more than 23 inds - have to have more than 10 by def
    ## all loci already have a minimum of 4 inds

    import re

    ## import file
    prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_klp_convert_labeled3.gphocs")
    #prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")
    lines = prob.readlines()
    prob.close()

    print lines[0:5],"##lines\n"

    ## set maximum and minimum individuals
    maxInd = 10
    minInd = 4

    ## open a new file for writing the info out as a .txt
    probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG.gphocs","w")

    #probout = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","w")

    outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_goodList_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG.txt","w")

    ## ID and count the loci with more than 23 individuals
        ## read a line (i)
        ## check the first three characters of the line to determine pop
        ## check which loci have non-N and non-gap
        ## if son > 10 or chi > 10, output it to a "bad list" with number each

    ## initialize counters and lists
    tempLoci = []
    firstLoci = True
    countSon = 0
    countChi = 0
    countLocus = 0

    ## print a placeholder for the number of loci
    print >>probout, "NUMLOCI"

    for i in range(len(lines)):
        if "locus" in lines[i]: ## if the line contains "locus" it a new locus
            if firstLoci == True: ## if the first locus
                firstLoci = False
                tempLoci.append(lines[i]) ## add the locus to the temp locus
                #print tempLoci,"##temp"
            else: ## if not a new locus
                #print tempLoci,"##temp"
                for j in range(len(tempLoci)): ## count the number of individuals in each desert
                    if tempLoci[j][0:3] == "Son": 
                        countSon = countSon + 1
                    if tempLoci[j][0:3] == "Chi":
                        countChi = countChi + 1
                #print countSon,countChi
                if countSon <= maxInd and countChi <= maxInd: ## if the loci are under the maximum
                    #print "less",
                    if countSon > minInd and countChi > minInd: ## and if the locu are over the minimum
                        #print "more"
                        print >>outfile, countLocus
                        for k in tempLoci: ## print each locus
                            print >>probout, k,
 
                            #print k,"##k"
                    #else: 
                        #print "not"
                        #x = 0
                    tempLoci = [] ## reset the temp loci
                else: ## if a new locus, reset the temp loci
                    #print "not"
                    tempLoci = []
                countSon = 0 ## reset the counts of individuals
                countChi = 0
                tempLoci.append(lines[i]) ## get a new temp locus
                countLocus += 1
                #print tempLoci
        else: ## get a new temp locus
            tempLoci.append(lines[i])
            #print tempLoci

    ## close the file
    probout.close()

    ## open the file to add the real number of loci
    replace = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG.gphocs","rU")
    #replace = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","r")
    read = replace.read()
    replace.close()

    print read[0:100]

    count = read.count("locus") ## count the loci
    #print count
    temp = re.sub("NUMLOCI",str(count),read) ## add the real number of loci
    print temp[0:50]

    ## overwrite the file with the replaced string
    replace = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_locuscap_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG.gphocs","w")
    #replace = open("C:/Users/Kaiya/Desktop/allelelocitestoutput.txt","w")
    print >>replace, temp
    replace.close()

    outfile.close()
