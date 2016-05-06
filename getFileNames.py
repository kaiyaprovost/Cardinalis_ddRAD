def getFileNames():
    '''
    returns file names in the folder this file is in
    '''
    import glob
    for filename in glob.glob("*.py"):
        print filename

if __name__ == "__main__":
    getFileNames()
