import pickle

dict = pickle.load(open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locicount.pkl","rb"))

testloci = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_labeled_locicount_test.txt","w")

testloci.write(str(dict))
