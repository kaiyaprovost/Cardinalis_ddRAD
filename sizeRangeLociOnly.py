if __name__ == "__main__":
    '''
    This code outputs a reduced subset of gphocs loci if you ALREADY have a list of the loci you want
    If you do NOT have this list, use popCapLoci_loci.py instead
    '''

    import re

    maxInd = 10
    minInd = 4

    goodLoci = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_labeled_goodList_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG.txt","r")
    good = goodLoci.readlines()
    goodLoci.close()

    print good[0:5]

    gphocsInfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_klp_convert_labeled3.gphocs","r")
    gphocs = gphocsInfile.readlines()

    print gphocs[0:5]

    gphocsInfile.close()

    outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/gphocs/cardcard_klp_convert_labeled3_reduced_max"+str(maxInd)+"_min"+str(minInd)+"DEBUG2.gphocs","w")

    locusCount = 0
    tempLoci = []
    locusGood = False

    for i in range(len(good)):
        good[i] = good[i].strip()
        ##print good[i]

    print >>outfile, str(len(good))

    for i in range(len(gphocs)):
        if "locus" in gphocs[i]:
            split = gphocs[i].split()
            if split[0][5:] in good:
                locusGood = True
                #print "keep it"
                tempLoci.append(gphocs[i].strip())
                #print tempLoci
            else:
                #print "remove it"
                locusGood = False
                for j in tempLoci:
                    print >>outfile, j
                tempLoci = []
                #print tempLoci
        else:
            ##print "not locus"
            if locusGood == True:
                tempLoci.append(gphocs[i].strip())
                #print tempLoci
            else:
                tempLoci = []
                #print tempLoci
             
    outfile.close()

