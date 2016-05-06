import csv
print "csv"
import matplotlib.pyplot as plt
print "plt"
import numpy as np
print "np"
from mpl_toolkits.basemap import Basemap
print "Base"

## read file
cardfile = open("C:/Users/Kaiya/Dropbox/Docs for Brian/THESIS/Raw Specimen Data/specimen_latlongs.csv")
# 
reader = csv.DictReader(cardfile)

## extract lat/long and ID
latStrings = []
longStrings = []
ident = []
desert = []

for row in reader:
    if row["latitude"] != "" :
        
        latStrings.append(row["latitude"])
        longStrings.append(row["longitude"])
        ident.append(row["Number"])
        desert.append(row["GROUP"])

cardfile.close()

latNum = []
longNum = []

for lat in latStrings:
    latNum.append(float(lat))
    print lat

for lon in longStrings:
    longNum.append(float(lon))
    print lon

print min(latNum),max(latNum) #18.1685 34.6706
print min(longNum),max(longNum) #-111.9397 -95.925472

xson = []
yson = []
xchi = []
ychi = []
xout = []
yout = []
xpyr = []
ypyr = []

for i in range(len(latNum)):
    if desert[i] == "SON":
        xson.append(longNum[i])
        yson.append(latNum[i])
    elif desert[i] == "CHI":
        xchi.append(longNum[i])
        ychi.append(latNum[i])
    elif desert[i] == "OUT":
        xout.append(longNum[i])
        yout.append(latNum[i])
    elif desert[i] == "PYRR":
        xpyr.append(longNum[i])
        ypyr.append(latNum[i])

xsonuni = []
ysonuni = []
sonsize = []
xchiuni = []
ychiuni = []
chisize = []

for i in range(len(xson)):
    if xson[i] not in xsonuni:
        sonsize.append(xson.count(xson[i]))
        xsonuni.append(xson[i])
        ysonuni.append(yson[i])

for i in range(len(xchi)):
    if xchi[i] not in xchiuni:
        chisize.append(xchi.count(xchi[i]))
        xchiuni.append(xchi[i])
        ychiuni.append(ychi[i])

xoutuni = [xout[0]]
youtuni = [yout[0]]
outsize = [3]
pyrsize = [1]


m = Basemap(llcrnrlat=15,urcrnrlat=35.5,llcrnrlon=-117,urcrnrlon=-95,lat_ts=30)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawmapboundary(fill_color="white")
m.fillcontinents(color="white")

#m.plot(xson,yson,'go',markersize=10)
#m.plot(xchi,ychi,'bo',markersize=10)
#m.plot(xout,yout,'ro',markersize=10)

m.plot(xsonuni[0],ysonuni[0],'ko',markeredgewidth='2',markeredgecolor="black",markerfacecolor='none',markersize=(10+(2*sonsize[0])),label=" 1 individual")
m.plot(xsonuni[1],ysonuni[1],'ko',markeredgewidth='2',markeredgecolor="none",markerfacecolor='none',markersize=(10+(2*sonsize[0])),label=" ")
m.plot(xsonuni[14],ysonuni[14],'ko',markeredgewidth='2',markeredgecolor="black",markerfacecolor='none',markersize=(10+(2*sonsize[14])),label=" 5 individuals")
m.plot(xsonuni[2],ysonuni[2],'ko',markeredgewidth='2',markeredgecolor="none",markerfacecolor='none',markersize=(10+(2*sonsize[0])),label="  ")
m.plot(xsonuni[4],ysonuni[4],'ko',markeredgewidth='2',markeredgecolor="black",markerfacecolor='none',markersize=(10+(2*sonsize[4])),label=" 17 individuals")

for i in range(len(outsize)):
    m.plot(xoutuni[i],youtuni[i],'ro',markeredgewidth='2',markeredgecolor="red",markerfacecolor='none',markersize=(10+(2*outsize[i]))) 
for i in range(len(chisize)):
    m.plot(xchiuni[i],ychiuni[i],'bo',markeredgewidth='2',markeredgecolor="blue",markerfacecolor='none',markersize=(10+(2*chisize[i])))
for i in range(len(sonsize)):
    m.plot(xsonuni[i],ysonuni[i],'go',markeredgewidth='2',markeredgecolor="green",markerfacecolor='none',markersize=(10+(2*sonsize[i])))
for i in range(len(pyrsize)):
    m.plot(xpyr[i]+.1,ypyr[i]+.1,'ko',markeredgewidth='2',markeredgecolor="black",markerfacecolor='none',markersize=(10+(2*pyrsize[i]))) 

plt.legend(loc = "lower left",numpoints=1,borderpad = 1.2,frameon=False)

plt.show()
