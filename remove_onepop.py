if __name__ == "__main__":

    ## list of single-population loci
    onepop = [0,1,8,29,37,51,109,130,163,188,235,319,338,441,464,499,582,622,663,680,715,717,725,740,747,792,811,867,881,921,981,1002,1022,1038,1099,1104,1114,1119,1183,1202,1241,1295,1447,1470,1474,1520,1551,1569,1602,1637,1732,1736,1746,1752,1762,1809,1849,1940,1941,1955,2156,2160,2236,2243,2283,2327,2406,2460,2522,2538,2563,2644,2661,2694,2742,2754,2819,2826,2988,2993,3025,3097,3122,3192,3210,3278,3308,3320,3347,3435,3461,3503,3538,3551,3552,3564,3578,3623,3673,3686,3712,3732,3815,3874,3891,3911,3943,4002,4039,4050,4084,4139,4169,4170,4202,4203,4254,4260,4315,4353,4413,4426,4513,4525,4526,4591,4613,4626,4722,4750,4842,4849,4878,4891,4896,4933,5054,5138,5142,5189,5215,5278,5284,5411,5412,5534,5540,5562,5567,5584,5606,5645,5656,5686,5702,5751,5779,5810,5853,5857,5893,5966,6059,6066,6097,6197,6267,6322,6338,6354,6363,6379,6417,6454,6483,6496,6525,6581,6626,6657,6718,6731,6754,6803,6804,6903,6909,6969,7023,7025,7065,7099,7136,7290,7291,7308,7330,7343,7370,7418,7466,7531,7537,7570,7648,7712,7715,7728,7752,7841,7877,7885,7947,7952,8008,8027,8032]

    ## open loci file and read it
    card = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci")
    lines = card.readlines()
    card.close()

    ## open files for writing the single and double population loci
    cardout_1pop = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_removed1pop.loci","w")
    cardout_2pop = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_only2pop.loci","w")

    ## begin a locus counter
    locusCount = 0

    ## go through each line
    for i in range(len(lines)):
        if locusCount in onepop: ## if the current locus is present in the single-population loci
            if lines[i][0]== ">": ## if the current line has data (FASTA style)
                print >>cardout_1pop, lines[i].strip() ## print the line to the single population file
            else: ## if the current line is not a data line
                locusCount = locusCount + 1 ## increase the locus count
                print >>cardout_1pop, "//" ## add a locus delimiter line
        else: ## if the current locus is not in the single-population list
            if lines[i][0]== ">": ## if the current line has data
                print >>cardout_2pop, lines[i].strip() ## print the line to the double-pop list
            else: ## if the current line is not a data line
                locusCount = locusCount + 1 ## increase the locus count
                print >>cardout_2pop, "//" ## add a locus delimiter line

    ## close the files
    cardout_1pop.close()
    cardout_2pop.close()
