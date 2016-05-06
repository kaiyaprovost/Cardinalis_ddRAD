def ambigExp(base):
    '''
    disambiguates the heterozygous ambiguity codes
    '''
    if base == "Y":
        expand = "CT"
    elif base == "R":
        expand = "AG"
    elif base == "W":
        expand = "AT"
    elif base == "S":
        expand = "GC"
    elif base == "K":
        expand = "TG"
    elif base == "M":
        expand = "CA"
    else:
        expand = base
    return expand

def ambigSimp(dataList):
    '''
    reambiguates lists of bases into their ambiguity codes
    '''
    if "A" in dataList:
        hasA = True
    else:
        hasA = False
    if "C" in dataList:
        hasC = True
    else:
        hasC = False
    if "G" in dataList:
        hasG = True
    else:
        hasG = False
    if "T" in dataList:
        hasT = True
    else:
        hasT = False
    if hasA:
        if hasG:
            if hasC:
                if hasT:
                    simp = "N"
                else:
                    simp = "V"
            else:
                if hasT:
                    simp = "D"
                else:
                    simp = "R"
        else:
            if hasC:
                if hasT:
                    simp = "H"
                else:
                    simp = "M"
            else:
                if hasT:
                    simp = "W"
                else:
                    simp = "A"
    else:
        if hasG:
            if hasC:
                if hasT:
                    simp = "B"
                else:
                    simp = "S"
            else:
                if hasT:
                    simp = "K"
                else:
                    simp = "G"
        else:
            if hasC:
                if hasT:
                    simp = "Y"
                else:
                    simp = "C"
            else:
                if hasT:
                    simp = "T"
                else:
                    simp = dataList
    return simp

def main():
    print "main"

if __name__ == "__main__":
    main()
    

    
    
    
    
    

    
    




                        
