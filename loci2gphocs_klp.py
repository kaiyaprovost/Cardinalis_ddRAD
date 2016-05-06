if __name__ == "__main__":
    #import pickle ## this is needed if you want to save the dict as a pickle file, otherwise not needed

    ## read in the file and read in the lines to iterate over
    prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_only2pop.loci")
    lines = prob.readlines()

    ## open a new file for writing the dictionary out as a .txt
    probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_klp_convert_labeled_only2pop.gphocs","w")

    ## gphocs format:
        ## at start of file, print number of loci
        ## begin a locus starting at locus 0
        ## on the same line, with a space, print the count of the number of lines in the locus
        ## on the same line, with a space, print the length of the locus
        ## print a name, then tab, then the data
        ## do that until all names in that locus are done
        ## repeat with a new locus

        ## totalLoci
        ## locusName numberInds lenLocus
        ## name1 (tab) data1
        ## name2 (tab) data2
        ## locusName numberInds lenLocus
        ## name3 (tab) data3
        ## name4 (tab) data4    

    ## loci format
        ## names start with a carat, then a tab, then the data
        ## names within the same loci continue until the //
        ## // is the locus delimiter

        ## >name1 (tab) data1
        ## >name2 (tab) data2
        ## //
        ## >name3 (tab) data3
        ## >name 4 (tab) data4

    ## count the total number of loci as measured by the delimiters
    ## print the count to the file as first line
    totalLoci = 0
    for i in range(len(lines)):
        totalLoci = totalLoci + lines[i].count("//")
    #print(totalLoci)
    print >>probout, totalLoci

    ## set up blank data structures and counters
    lociCount = 0 ## the current counter of the number of loci
    lociCountList = []
    namedataList = []
    firstLine = True
    sequences = []

    # begin to read data
    for i in range(len(lines)): ## iterate over the lines
        if lines[i][0]== ">": ## if the data starts with a ">" that means it is the name of an individual with the data following
            #print "name"
            fullLines = lines[i][1:].strip()
            convertLines = fullLines.replace("-","N") ## changes gaps from gap to N

            splitLines = convertLines.split() ## splits the line into the name and the base pairs
                   
            name = splitLines[0].strip() ## takes only the name of the split, without the ">" in front of the name
            data = splitLines[1].strip() ## takes all the bases

            printLines = name+"\t"+data

            sequences.append(printLines) ## add the name and data to the sequences

            if firstLine == True:
                #print "firstline"
                lenData = len(data)
                

            #print len(data)

            #print >>probout, "locus"+str(lociCount), splitLines 

            if i == len(lines)-1: ## if the line is the last line
                lociCount = lociCount + 1 ## increase the loci counter by 1

            firstLine = False
                
        else: ## if the line does not start with ">" it is a "//" and a loci delimiter, indicating the end of the locus
            #print "loci delimiter"

            #print "ALL THE THINGS TO THE FILE"

        ## locusCount numInd lenData
        ## name1 (tab) data1
        ## name2 (tab) data2

            numInd = len(sequences) ## the number of sequences is the number of individuals at the locus
            
            print >>probout, 'locus'+ str(lociCount), str(numInd), str(lenData)
            for j in range(len(sequences)):
                print >>probout, sequences[j]


            #print "RESET ALL THE THINGS"

            lociCount = lociCount + 1 ## increase the loci counter by 1
            firstLine = True ## set back to first line
            sequences = [] ## empty the sequences
            #print "delimit"
            lenData = 0 ## set the length of the data back to zero


    ## close the file you opened to get the lines
    prob.close()

    ## close the new file
    probout.close()
