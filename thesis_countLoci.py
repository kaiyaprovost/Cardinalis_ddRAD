def countLoci(lines):
    '''
    Input lines of a LOCI or ALLELES file, outputs dictionary of individuals in each locus.
    '''
    ## steps:
        ## count the number of loci
        ## iterate through lines
        ## collect >names, discard data
        ## when hit //, the locus delimiter
        ## associate names with locus
        ## begin next locus

    ## set up blank data structures and counters
    lociCount = 0 ## the current counter of the number of loci
    lociDict = {} ## an empty dictionary to be populated with the loci number and individuals within the dictionary
    namesList = [] ## an empty list of names of individuals

    # begin to read data
    for i in range(len(lines)): ## iterate over the lines
        if lines[i][0]== ">": ## if the data starts with a ">" that means it is the name of an individual with the data following
            #print "name"
            splitLines = lines[i].split() ## splits the line into the name and the base pairs
            name = splitLines[0][1:] ## takes only the name of the split, without the ">" in front of the name
            namesList.append(name) ## adds the name to the running list of names
            #print(name)
            #print(namesList)
            if i == len(lines)-1: ## if the line is the last line
                lociDict[lociCount] = namesList ## for the current counter of the number of loci, the corresponding value in the dictionary is the list of names
                lociCount = lociCount + 1 ## increase the loci counter by 1
                #print(lociCount)
                #print "end file"
                #print(lociDict)
                
        else: ## if the line does not start with ">" it is a "//" and a loci delimiter, indicating the end of the locus
            #print "loci delimiter"
            lociDict[lociCount] = namesList ## for the current counter of the number of loci, the corresponding value in the dictionary is the list of names
            #print(lociDict)
            lociCount = lociCount + 1 ## increase the loci counter by 1
            #print(lociCount)
            namesList = [] ## reset the list of names to blank

    return lociDict

def main():

    ## read in the file and read in the lines to iterate over
    thamno = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/Thamnophilidae/Raw Data/c85d6m4p3.loci")
    lines = thamno.readlines()

    ## close the original file you opened to get the lines
    thamno.close()

        #card = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci")
        #lines = card.readlines()

        #prob = open(r"C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt")
        #lines = prob.readlines()

    ## open a new file for writing the dictionary out as a .txt
    thamnout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/Thamnophilidae/Raw Data/thamno_locicount.txt","w")
    thamnout.write(str(lociDict))

    ## close the new file
    thamnout.close()

    #outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locicount.pkl","w")
    #pickle.dump(lociDict,outfile,0)

    #probout = open("C:/Users/Kaiya/Desktop/scratch_loci_count.txt","w")
    #probout.write(str(lociDict))

    #prob.close()
    #probout.close()

    #card.close()
    #outfile.close()

if __name__ == "__main__":
    main()
