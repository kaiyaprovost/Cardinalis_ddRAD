def mean(listA):
	'''
	Returns the mean of a list
	'''
	m = float(sum(listA)) / float(len(listA))
	return m

def stdev(listA):
	'''
	Returns the standard deviation of a list
	'''
	import math
	m = mean(listA)
	difs = [x-m for x in listA]
	sqdifs = [d*d for d in difs]
	ssd = sum(sqdifs)
	var = ssd / (len(listA)-1)
	stdev = math.sqrt(var)
	return stdev

def importClusterDict(string):
	'''
	Imports a file and returns a dictionary containing information about k-clustering, pool identity, barcode identity, etc
	'''
	poolfile = open(string,"rU")
	lines = poolfile.readlines()
	poolfile.close()
	clusterDict = {}
	for i in lines:
		k1,loc,iden,pool,barcode,des = i.strip().split(",")
		#print k1
		if k1 != "K1AVG":
			clusterDict[iden] = [float(k1),pool,int(barcode),des[0:3]]
	return clusterDict

def getPerms(indexList):
	'''
	Gets all possible permutations of either pools or barcodes
	'''
	from itertools import permutations
	permuteList = []
	first = True
	for i in permutations(indexList,len(indexList)):
		if first == True:
			original = i
			first = False
		permuteList.append(i)
	return permuteList

def getDesAvgSD(clusterDict):
	'''
	Returns the average standard deviation of k-cluster assignment for each desert
	'''
	son = []
	chi = []
	out = []
	for i in clusterDict:
		desert = clusterDict[i][-1]
		clust = clusterDict[i][0]
		if desert == "Son":
			son.append(clust)
		elif desert == "Chi":
			chi.append(clust)
		elif desert == "Out":
			out.append(clust)
		else:
			print "error"
	meanSon = mean(son)
	sdSon = stdev(son)
	meanChi = mean(chi)
	sdChi = stdev(chi)
	meanOut = mean(out)
	sdOut = stdev(out)
	return [meanSon,sdSon],[meanChi,sdChi],[meanOut,sdOut]

def compareDictMSD(orgDict,dict2):
	'''
	Compares mean standard deviations for each desert between two dictionaries
	'''
	son1,chi1,out1 = getDesAvgSD(orgDict)
	son2,chi2,out2 = getDesAvgSD(dict2)
	sonDevDif = son1[1] - son2[1] ## if positive, permutation is better
	chiDevDif = chi1[1] - chi2[1]
	outDevDif = out1[1] - out2[1]
	#print sonDevDif,chiDevDif,outDevDif
	sumSD = sum([sonDevDif,chiDevDif,outDevDif])
	return sumSD,son2,chi2,out2 ## returns the sum SD dif and the means of the new cluster

def allDictPermutations(clusterDict,indexList,outfile):
	'''
	Imports a dictionary, swaps pairs of pools/barcodes, and returns the differences in standard deviation between the swapped and the original dictionary
	'''
	## import original dictionary
	## import index List
	## import outfile
	import copy

	## create a copy of the dictionary in case of fuckups
	origDict = copy.deepcopy(clusterDict)

	## set up the file to print to
	print >>outfile, "PERMUTATION","\t","PAIRS SWAPPED","\t","SUM DIF IN SD","\t","SON MEAN/SD","\t","CHI MEAN/SD","\t","OUT MEAN/SD","\t","ACTUAL PERMUTE"
	
	## create permutations of index List
	permuteList = getPerms(indexList)

	## get num of permutations
	permLen = len(permuteList)
	
	## for each permutatiion:
	#for i in range(10): ## DEBUGGING
		## change from tuple to list
		#print "--------------------------------"
		#perm = list(permuteList[i])
		#print "perm:",perm,"\t"+"orig:",indexList
	for permTUP in permuteList:
		## change from tuple to list
		perm = list(permTUP)
		
		## create a copy of the dictionary to swap
		swapDict = copy.deepcopy(clusterDict)
		

		## check the permutation against the original index
		if perm == indexList:
			## the permutation is the original list
			#print "\t is org"
			swapDict = copy.deepcopy(origDict)
			swapsMade = []
		else:
			## the permutation is a permutation
			#print "\t is perm"
			## setup swapsMAde list
			swapsMade = []
			
			## for each barcode in the permutation:
			for barIndex in range(len(perm)):
				#print "\t bar index",barIndex,
				## find the corresponding barcode in the permutation
				barcodeSwap = perm[barIndex]
				## find the corresponding barcode in the original
				barcodeOrig = indexList[barIndex]
				#print "\t swapBar",barcodeSwap,
				#print "\t origBar",barcodeOrig,
				if barcodeSwap == barcodeOrig:
					## if the barcodes are the same, do nothing
					x = 1
					#print "MATCH"
				else:
					## get the keys matching those barcodes
					#print "SWAP"
					swapKeyTO = []
					origKeyFROM = []
					for key in origDict:
						#print "\t key",key,
						barcode = int(origDict[key][1].replace("P",""))
						#print "pool",barcode,
						#print barcodeSwap,barcode==barcodeSwap
						#print "Type, barcode",type(barcode),"swap",type(barcodeSwap)
						if barcode == barcodeSwap:
							## if the found barcode matches a barcode to swap:
							swapKeyTO.append(key)
							#print "\t\t added to SWAP",barcode
							## add the key to the list of keys to swap
						if barcode == barcodeOrig:
							## if the found barcode matches an original barcode to swap
							origKeyFROM.append(key)
							#print "\t\t added to ORIG",barcode
							## add the key to the list of keys to swap
					swapKeyTO.sort()
					origKeyFROM.sort()
					## overwrite the swapDictionary barcode and k value
					## with the originalDictionary barcode and k value
					
					for i in range(len(swapKeyTO)):
						## for each key to swap
						## check that the pools match
						toKey = swapKeyTO[i]
						fromKey = origKeyFROM[i]
						#print "tokey",toKey
						#print "fromkey",fromKey
						if toKey[-3:] == fromKey[-3:]:
							## in the swapDict only, change the toKey's barcode and k
							## to the fromKey's barcode and k
							toClust = swapDict[toKey][0]
							fromClust = origDict[fromKey][0]
							
							toPool = swapDict[toKey][1]
							fromPool = origDict[fromKey][1]

							toBarcode = swapDict[toKey][2]
							fromBarcode = origDict[fromKey][2]

							toDes = swapDict[toKey][3]
							fromDes = origDict[fromKey][3]

							#print "BEFORE DICT",toKey,swapDict[toKey]
							swapDict[toKey] = [fromClust,fromPool,toBarcode,toDes]
							#print "AFTER DICT",toKey,swapDict[toKey]
							## add the swapped barcode to swapsMade list if it isnt in there yet
					swapsMade.append([barcodeSwap,barcodeOrig])
		
		## when done swapping the barcodes
		## pull out the mean/stdevs for each desert
		## and compare the means to the original
		sdDif,sonM,chiM,outM = compareDictMSD(origDict,swapDict)
		## print to a file the hypothetical permutation, actual permutation,
			## standard dev change, means/sd for each desert
		#print "CHECK MATCH:"
		#print perm
		print >>outfile, perm,"\t",swapsMade,"\t",sdDif,"\t",sonM,"\t",chiM,"\t",outM,"\t",
		actualOrder = []
		for i in ["P1_P1F_01","P2_P1F_01","P3_P1F_01","P4_P1F_01","P5_P1F_01","P6_P1F_01","P7_P1F_01","P8_P1F_01","P9_P1F_01"]:
			#print "\t",i,swapDict[i][2],
			#print swapDict.get(i),"GET"
			tempValues = swapDict.get(i)
			actualOrder.append([tempValues[1],i])
		actualOrder.sort()
		#print "ACTUAL ORDER"
		for j in actualOrder:
			print >>outfile, (j[1][0:2].replace("_","").replace("P","")),
		print >>outfile,"\n",
		#print

if __name__ == "__main__":
	## read file
	#string = "C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_testCSV.csv"
	string = "C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_CSV.csv"
	clusterDict = importClusterDict(string)
	#print clusterDict

	#print clusterDict.get("P4_P1F_01")

	indexList = [1,2,3,4,5,6,7,8,9]
	outfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_PERMSD_POOLS.csv","w")
	
	allDictPermutations(clusterDict,indexList,outfile)

	outfile.close()


