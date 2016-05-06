def lociAmbigFilter(lines,outfile,thresh):
    '''
    Finds loci with % non-ambiguous sequences above the threshhold
    '''
    ## set up counters and containers for loci
    ambigCount = 0 ## counts number of ambiguous loci - gaps, N, or n, but not the ambiguity codes
    baseCount = 0 ## counts number of non-ambiguous loci - anything not the above
    tempLocus = []## temporary container for individual loci

    ## for each individual line of data
    for line in lines: 
        ## take off the trailing newline character
        strip = line.strip() 
        ## if the first character is ">", indicating a name
        if strip[0] == ">":
            ## if the name is the first one (in that there are no stored loci)
            if tempLocus == []:
                ## store the name
                tempLocus.append(strip) 
            else:
                ## if there are stored loci
                ## if the percent real bases is above the threshhold
                if baseCount/float(baseCount+ambigCount) >= thresh:
                    ## begin printing the lines of the stored locus to the outfile
                    for i in tempLocus:
                        ## if it is a name line
                        if i[0] == ">":
                            ## print the name plus the number of real bases over the total bases
                            #print >>outfile, i+"_"+str(baseCount)+"/"+str(baseCount+ambigCount)
                            ## print the name
                            print >>outfile, i
                        else:
                            ## otherwise, print the line
                            print >>outfile, i
                #else:
                    #print "BAD"
                ## after all of the data is printed to the outfile
                ## reset the counters and store the next line
                tempLocus = []
                tempLocus.append(strip)
                ambigCount = 0
                baseCount = 0
                
        else: ## if the line is not a name
            ## store the line
            tempLocus.append(strip)
            ## for each base character in the line
            for character in strip:
                ## if the character is ambiguous or gap
                if character in ["N","n","-"]:
                    ## increase the ambiguity count
                    ambigCount += 1
                else:
                    ## if the character is not
                    ## increase the "real" bases count
                    baseCount += 1

def main():
    ## import modules
    import sys ## allows you to add command line arguments
    import os ## allows you to get the current folder
    import glob ## allows you to get all of the fasta files

    ## set flags from command line
    ## USAGE: python brianFasta.py threshhold

    ## set threshhold
    try:
        thresh=float(sys.argv[1])
        print("Threshhold is:",thresh)
    except:
        thresh = 0.50
        print('Threshhold not entered - defaulting to: '+str(thresh))

    ## get current folder
    folder = os.getcwd()

    ## make an output folder "\thresh###" if it doesn't exist
    if not os.path.exists(folder+"/"+"thresh"+str(thresh)):
        os.makedirs(folder+"/"+"thresh"+str(thresh))

    ## get files in folder
    filelist = []
    print "FILES:"
    for filename in glob.glob("*.fa"):
        print filename
        ## add the filename without the .fa ending to a list
        filelist.append(filename[0:-3])

    ## perform fasta check for each file in the folder
    for i in filelist:
        temp = open(folder+"/"+i+".fa","rU") ## open the file
        lines = temp.readlines() ## read the lines of the file's data
        temp.close() ## close the file

        ## create an outfile to print the new extracted data
        outfileString = folder+"/"+"thresh"+str(thresh)+"/"+i+"_"+str(thresh)+"thresh.fa"
        outfile = open(outfileString,"w")
        
        ## run the fasta filter function on the data
        lociAmbigFilter(lines,outfile,thresh)

        ## close and save the new printed loci
        outfile.close()

if __name__ == "__main__":
    main()
