if __name__ == "__main__":
    ## read in a list of loci
	lociInfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled.loci","r")
	lociInfileLines = lociInfile.readlines()
	lociInfile.close()

	## initialize an outfile
	lociOutfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_SPLIT.loci","w")

	for line in lociInfileLines:
		if line[0] == ">": ## if the line contains base pair data
			splitLine = line.split() ## split the line
			name = splitLine[0]
			gene = splitLine[1]
			for site4 in range(0,len(gene)-4): ## iterate over chunks of 4 base pairs
				if gene[site4:site4+4] == "nnnn": ## if the chunk is the forward/reverse splitter
					fwd = gene[:site4] ## take the forward read
					rev = gene[site4+4:] ## take the reverse read
					print >>lociOutfile, name+"-FWD\t"+fwd ## print the forward read and rename
					print >>lociOutfile, name+"-REV\t"+rev ## print the reverse read and rename
		else: ## if the line is a locus delimiter
			print >>lociOutfile, line, ## print the line
            
	## close the file
	lociOutfile.close()
