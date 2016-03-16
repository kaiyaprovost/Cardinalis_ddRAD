import csv
import re

def cardNameChange(namesFileString,dataFileString):
    convertList = open(namesFileString,"r")
    reader = csv.DictReader(convertList)

    dataList = open(dataFileString,"r")
    data = dataList.read()
    dataList.close()

    #print data[0:500]

    #for row in reader:
    #    print row

    convertList.close()

def fixZerosFunc(dataFileString,outFileString,dataType="alleles",outDelimit=" "):
    print "WARNING: THIS PROGRAM WILL CONVERT WHITESPACE"
    check = str(raw_input("DO YOU WISH TO CONTINUE? Y/N: "))
    if check == "N":
        print "PROGRAM TERMINATED"
    if check == "Y":
        ## acceptable types: loci, alleles, gphocs
        card = open(dataFileString,"r")
        lines = card.readlines()
        card.close()

        outfile = open(outFileString,"w")

        #print dataType
        #print lines[0]
        
        #if dataType == "loci":

        if dataType == "alleles":
            for i in range(len(lines)):
                if lines[i][0] == ">":
                    #print r(lines[i])
                    splitLines = lines[i].split(" ")
                    #print splitLines[0]
                    #print splitLines[0][:-2][-2:]
                    if splitLines[0][:-2][-2:] == "_1":
                        ## data has _1 format instead of _01
                        splitLines[0] = str(splitLines[0][:-4])+"_01"+splitLines[0][-2:]
                        del splitLines[1]
                    joined = outDelimit.join(splitLines)
                    print >>outfile, joined,
                else:
                    print >>outfile, lines[i],
        
        
        #if dataType == "gphocs":
        else:
            print "FILE TYPE NOT ACCEPTED"

        outfile.close()
    else:
        print "INPUT "+str(check)+" NOT ACCEPTED, PROGRAM TERMINATED"

listOfNames = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/lookup_script.csv"

listOfData = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard.alleles"

listOfZeroData = "C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_zeroFix_tabbed.alleles"

#cardNameChange(listOfNames,listOfData)
fixZerosFunc(listOfData,listOfZeroData,dataType="alleles",outDelimit=" ")
        
### iterate over each of the possible Lookup_IDs (72 is the number of individuals in our pool, so it is 72)
##for (i in 1:73) {
##    ## when a Lookup_ID is found in the imported file, replace it with the Specimen_ID
##    ## make this into the outfile
##    outfile = gsub(pattern=lookup_script$Lookup_ID[i],
##                   replace=lookup_script$Specimen_ID[i],
##                   x=filename)
##    
##    ## when a Pool_ID is found in the imported file, replace it with the Specimen_ID
##    ## update the outfile with new search
##    outfile = gsub(pattern=lookup_script$Pool_ID[i],
##                   replace=lookup_script$Specimen_ID[i],
##                   x=outfile) 
##    
##    ## to begin loop again, set the filename and outfile to be the same thing
##    filename = outfile
##}
##
#### export the outfile as a labeled file with same format as original
##writeLines(outfile,con="~/Columbia/Thesis/THESIS DATA/cardcard_labeledtabs2.alleles")
