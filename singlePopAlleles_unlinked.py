## read in the file and read in the lines to iterate over
prob = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.unlinked_snps")

#prob = open(r"C:/Users/Kaiya/Desktop/allelelocitest.txt")

lines = prob.readlines()

## open a new file for writing the info out as a .txt
probout = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_allele_information.txt","w")

#probout = open("C:/Users/Kaiya/Desktop/allelocitestoutput.txt","w")

## steps:
    ## read a line (i) ## done
    ## check the first 3 characters of the line to get the population ## done
    ## read the Nth character in the line - that is the locus ## done
## go to that locus (j) within a population list
    ## if the Nth character is not already associated with that pop, add it to the pop for that locus
    ## if the Nth character is already associated, do nothing

countLine = 0
countLoci = 0
firstSon = 0
firstChi = 0
firstOut = 0

sonList = [None] * len(lines[1].split()[1])
chiList = [None] * len(lines[1].split()[1])
outList = [None] * len(lines[1].split()[1])

for i in range(len(lines)):
    if countLine != 0:
        splitLines = lines[i].split()
        #print splitLines
        if splitLines[0][0:3] == "Son":
            for j in range(len(splitLines[1])):
                if splitLines[1][j] in ["Y","R","K","W","S","M"]:
                    diploid = True
                else:
                    diploid = False
                x = sonList[j]
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
                sonList[j] = x

        if splitLines[0][0:3] == "Chi":
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

        if splitLines[0][0:3] == "Out":
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
    else:
        splitLines = ""
    countLine = countLine + 1 

def compareAlleles(sonList,chiList,outList,filename):
    sumJ = 0
    sumK = 0
    sumM = 0
    print >>filename, "POP","\t","LOCUS","\t","ALLELE"
    lenSon = len(sonList)
    lenChi = len(chiList)
    lenOut = len(outList)
    if lenSon != lenOut or lenChi != lenOut or lenSon != lenChi:
        return "Error! Lists must be same length of loci"
    else:
        locusLen = lenSon
    for locus in range(locusLen):
            for j in sonList[locus]:
                if j not in chiList[locus] and j not in outList[locus]:
                    ## j is unique allele
                    print >>filename, "son"+"\t"+"locus"+str(locus)+"\t"+str(j)
                
                sumJ = len(j) + sumJ
            for k in chiList[locus]:
                if k not in sonList[locus] and k not in outList[locus]:
                    ## k is unique allele
                    print >>filename, "chi"+"\t"+"locus"+str(locus)+"\t"+str(k)
                sumK = len(k) + sumK
            for m in outList[locus]:
                if m not in sonList[locus] and m not in chiList[locus]:
                    print >>filename, "out"+"\t"+"locus"+str(locus)+"\t"+str(m)
                sumM = len(m) + sumM 
    print "son alleles","chi alleles","out alleles"
    print sumJ,sumK,sumM
    return sumJ,sumK,sumM
                
compareAlleles(sonList,chiList,outList,probout)


## close the file you opened to get the lines
prob.close()

## close the new file
probout.close()
