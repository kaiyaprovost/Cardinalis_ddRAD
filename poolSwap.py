def mean(listA):
	m = float(sum(listA)) / float(len(listA))
	return m

def stdev(listA):
	import math
	m = mean(listA)
	difs = [x-m for x in listA]
	sqdifs = [d*d for d in difs]
	ssd = sum(sqdifs)
	var = ssd / (len(listA)-1)
	stdev = math.sqrt(var)
	return stdev

def getToSwap(index1,index2,clusterDict,swap):
	import copy
	dup = copy.deepcopy(clusterDict)
	index1KEY = []
	index2KEY = []
	index1VAL = []
	index2VAL = []
	for j in dup:
		#print
		#print j,":",
		i = dup[j][2] ##gets barcode
		#print i,"i"
		if i == index1:
			index1KEY.append(j)
			index1VAL.append(dup[j])
			#print index1KEY,index1VAL,"index1"
		if i == index2:
			index2KEY.append(j)
			index2VAL.append(dup[j])
			#print index2KEY,index2VAL,"index2"
		#print
	index1KEY.sort()
	index2KEY.sort()
	return index1KEY,index2KEY,index1VAL,index2VAL

def swapFunction(keys1,keys2,vals1,vals2,clusterDict,swap):
	import copy
	dup = copy.deepcopy(swap)
	org = copy.deepcopy(clusterDict)
	#print "copied"
	#print keys1,"keys1"
	#print keys2,"keys2"
	#print "----"
	for i in range(len(keys1)):
		#print i,"i:"
		#print "before",keys1[i],dup[keys1[i]],keys2[i],dup[keys2[i]]
		tempswap1 = org[keys1[i]]
		tempswap2 = org[keys2[i]]

		#print "before",tempswap1,tempswap2
		tempswap1[0],tempswap2[0] = tempswap2[0],tempswap1[0]
		tempswap1[2],tempswap2[2] = tempswap2[2],tempswap1[2] ## successfully changing
		#print "after",tempswap1,tempswap2

		dup[keys1[i]] = tempswap1
		dup[keys2[i]] = tempswap2
		#print "after",keys1[i],dup[keys1[i]],keys2[i],dup[keys2[i]]
		#print
	#print "END SWAP FUNCTION ----------------------------------------------@@"
	return dup

def getPerms(indexList):
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

def swapList(list1,list2,clusterDict,swap):
	import copy
	#print "list1",list1
	#print "list2",list2
	if len(list1) != len(list2):
		print "ERROR"
		return []
	dup = copy.deepcopy(swap)
	org = copy.deepcopy(clusterDict)
	#print "original dict"
	#print org
	#print
	swappedList = []
	swappedPairs = []
	for i in range(len(list1)):
		#print "I",i
		if list1[i] != list2[i] and list1[i]:
			A,B = list1[i],list2[i]
			#print "A",A,"B",B
			#if A not in swappedList and B not in swappedList:
			if [A,B] not in swappedPairs:
				#swappedList.append(A)
				#swappedList.append(B)
				swappedPairs.append([A,B])
				#swappedPairs.append([B,A])
				#print swappedPairs,"swapped"
				keys1,keys2,vals1,vals2 = getToSwap(A,B,org,dup) ## GET TO SWAP
				#print keys1,keys2,vals1,vals2, "LISTI"
				#print
				dup = swapFunction(keys1,keys2,vals1,vals2,org,dup) ## SWAP FUNCTION
				#print "DUP",dup
				#print dup == org
			#else:
				#print "already swapped"
	#print "done"
	if dup == clusterDict:
		print "\tERROR, NO SWAP--------------------------"
	return dup,swappedPairs

def compareDictMSD(orgDict,dict2):
	son1,chi1,out1 = getDesAvgSD(orgDict)
	son2,chi2,out2 = getDesAvgSD(dict2)
	sonDevDif = son1[1] - son2[1] ## if positive, permutation is better
	chiDevDif = chi1[1] - chi2[1]
	outDevDif = out1[1] - out2[1]
	#print sonDevDif,chiDevDif,outDevDif
	sumSD = sum([sonDevDif,chiDevDif,outDevDif])
	return sumSD,son2,chi2,out2 ## returns the sum SD dif and the means of the new cluster

def allDictPermutations(clusterDict,indexList,outfile):
	import copy
	swap = copy.deepcopy(clusterDict)
	print >>outfile, "original list:","\t",indexList
	permuteList = getPerms(indexList)
	permLen = len(permuteList)
	#print permLen,"PERMLEN"
	print >>outfile, "num permutations:","\t",permLen
	print >>outfile, "NEW PERMUTATION","\t","PAIRS SWAPPED","\t","SUM DIF IN SD","\t","SON MEAN/SD","\t","CHI MEAN/SD","\t","OUT MEAN/SD"
	for permTUP in permuteList:
		perm = list(permTUP)
		#print perm,indexList,perm==indexList
		if perm != indexList:
			swappedDict,swappedPairs = swapList(perm,indexList,clusterDict,swap)
			#print swappedDict,"\n",swappedPairs,"DICT/PAIRS"
			sdDif,sonM,chiM,outM = compareDictMSD(clusterDict,swappedDict)
			#print sdDif
			print >>outfile, perm,"\t",swappedPairs,"\t",sdDif,"\t",sonM,"\t",chiM,"\t",outM,"\t",
			for i in ["P1_P1F_01","P1_P1F_2","P1_P1F_3","P1_P1F_4","P1_P1F_5","P1_P1F_6","P1_P1F_15","P1_P1F_16"]:
				print >>outfile,swappedDict[i][2],
			print >>outfile, "\n",
		else:
			sdDif,sonM,chiM,outM = compareDictMSD(clusterDict,clusterDict)
			print >>outfile, perm,"\t","NONE","\t",sdDif,"\t",sonM,"\t",chiM,"\t",outM
##		print "ARE SWAP AND CLUST EQUAL?"
##		print swappedDict == clusterDict
##		for key in swappedDict:
##			print key, swappedDict[key],clusterDict[key]


if __name__ == "__main__":
	#import csv
	## read file
	poolfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_testCSV.csv","rU")
	#poolfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_CSV.csv","rU")
	lines = poolfile.readlines()
	poolfile.close()

	clusterDict = {}
	for i in lines:
		k1,loc,iden,pool,barcode,des = i.strip().split(",")
		#print k1
		if k1 != "K1AVG":
			clusterDict[iden] = [float(k1),pool,int(barcode),des[0:3]]

	indexList = [1,2,3,4,5,6,15,16]
##	#perm = [4,6,3,2,16,5,1,15]
##	perm = [16,15,6,5,4,3,2,1]
##
##	a,b,c,d = getToSwap(1,4,clusterDict)
##	print a,"\n"
##	print b,"\n"
##	print c,"\n"
##	print d,"\n"
##	print "--------------------"
##
##	e = swapFunction2(a,b,clusterDict)
	
	#outfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_PERMSD.csv","w")
	outfile = open("C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Raw Specimen Data/QUALITY_CHECK_PERMSD_test.csv","w")
	
	allDictPermutations(clusterDict,indexList,outfile)

	outfile.close()
