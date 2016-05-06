if __name__ == "__main__":
    
    ## import needed files
    import csv
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.basemap import Basemap
    from matplotlib.patches import Polygon
    import random
    from matplotlib.collections import PatchCollection
    from matplotlib.patches import PathPatch

    ## if needed, add a random seed for replicability
    #random.seed(120412)

    ## read file
    cardfile = open("C:/Users/Kaiya/Dropbox/Docs for Brian/THESIS/Raw Specimen Data/specimen_latlongs_county.csv")
    reader = csv.DictReader(cardfile)

    ## extract lat/long and ID
    latStrings = []
    longStrings = []
    ident = [] ## the individual identity
    desert = [] ## the desert the individual belongs to
    county = [] ## the county the individual belongs to

    ## extract the data
    for row in reader:
        if row["latitude"] != "" :        
            latStrings.append(row["latitude"])
            longStrings.append(row["longitude"])
            ident.append(row["Number"])
            desert.append(row["GROUP"])
            county.append(row["County"])

    cardfile.close()

    ## convert the lat/longs to numbers
    latNum = []
    longNum = []
    for lat in latStrings:
        latNum.append(float(lat))
        #print lat
    for lon in longStrings:
        longNum.append(float(lon))
        #print lon

    ## if needed, get the maximum and minimum latitude for printing the map
    #print min(latNum),max(latNum) #18.1685 34.6706
    #print min(longNum),max(longNum) #-111.9397 -95.925472

    ## initalize lists for point storage
    ## x = long, y = lat, c = county
    xson = []
    yson = []
    cson = []

    xchi = []
    ychi = []
    cchi = []

    xout = []
    yout = []
    cout = []

    xpyr = []
    ypyr = []

    ## populate the lists by desert type
    for i in range(len(latNum)):
        if desert[i] == "SON":
            xson.append(longNum[i])
            yson.append(latNum[i])
            cson.append(county[i])
        elif desert[i] == "CHI":
            xchi.append(longNum[i])
            ychi.append(latNum[i])
            cchi.append(county[i])
        elif desert[i] == "OUT":
            xout.append(longNum[i])
            yout.append(latNum[i])
            cout.append(county[i])
        elif desert[i] == "PYRR":
            xpyr.append(longNum[i])
            ypyr.append(latNum[i])

    ## create jittered points so that points don't stack
    xsonjit = []
    ysonjit = []
    xchijit = []
    ychijit = []
    xoutjit = []
    youtjit = []

    ## jitter the points for each desert
    for i in range(len(xson)):
        if xson[i] not in xsonjit: ## if the point isn't in the list yet, don't jitter it
            xsonjit.append(xson[i])
            ysonjit.append(yson[i])
        else: ## if the point is in the list, jitter it randomly up and right
            xsonjit.append(xson[i]+random.uniform(0.2,0.5))
            ysonjit.append(yson[i]+random.uniform(0.2,0.5))
    for i in range(len(xchi)):
        if xchi[i] not in xchijit:
            xchijit.append(xchi[i])
            ychijit.append(ychi[i])
        else:
            xchijit.append(xchi[i]-random.uniform(0.2,0.5))
            ychijit.append(ychi[i]-random.uniform(0.2,0.5))
    for i in range(len(xout)):
        if xout[i] not in xoutjit:
            xoutjit.append(xout[i])
            youtjit.append(yout[i])
        else:
            xoutjit.append(xout[i]+random.uniform(0.2,0.5))
            youtjit.append(yout[i]+random.uniform(0.2,0.5))

    ## create the map
    m = Basemap(llcrnrlat=17,urcrnrlat=35.5,llcrnrlon=-113,urcrnrlon=-95,lat_ts=30)
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    m.drawmapboundary(fill_color=(0.5,0.5,0.5))
    m.fillcontinents(color="white")

    ## plot the jittered points, different colors/shapes for each desert
    m.plot(xsonjit,ysonjit,'go',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(0,1,0),markersize=10)
    m.plot(xchijit,ychijit,'bs',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(0,0,1),markersize=10)
    m.plot(xoutjit,youtjit,'rd',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(1,0,0),markersize=10)
    m.plot(float(xpyr[0])+0.2,float(ypyr[0])+0.2,'y^',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(1,1,0),markersize=10)

    ## save the figure and plot
    plt.savefig('C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/Field Work/Point and Dist Data/test.png',dpi=300, bbox_inches='tight')
    plt.show()
