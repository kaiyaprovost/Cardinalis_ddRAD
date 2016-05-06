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

    print "loaded"

    ## if needed, add a random seed for replicability
    #random.seed(120412)

    ## read file
    cardfile = open("C:/Users/Kaiya/Dropbox/Docs for Brian/THESIS/Raw Specimen Data/songs_latlongs.csv")
    reader = csv.DictReader(cardfile)

    ## extract lat/long and ID
    latStrings = []
    longStrings = []
    loc = [] ## the individual identity
    group = [] ## the desert the individual belongs to

    ## extract the data
    for row in reader:
        if row["latitude"] != "" :        
            latStrings.append(row["latitude"])
            longStrings.append(row["longitude"])
            loc.append(row["Locality"])
            group.append(row["GROUP"])

    cardfile.close()

    print "read"

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
    #print min(latNum),max(latNum) #30 35
    #print min(longNum),max(longNum) #-115 -103

    ## initalize lists for point storage
    ## x = long, y = lat, c = county

    disx = []
    disy = []

    locx = []
    locy = []

    nulx = []
    nuly = []

    acrx = []
    acry = []

    ## populate the lists by desert type
    for i in range(len(latNum)):
        if group[i] == "DIS":
            disx.append(longNum[i])
            disy.append(latNum[i])
        elif group[i] == "LOC":
            locx.append(longNum[i])
            locy.append(latNum[i]-0.2)
        elif group[i] == "NUL":
            nulx.append(longNum[i])
            nuly.append(latNum[i]+0.2)
        elif group[i] == "ACR":
            acrx.append(longNum[i])
            acry.append(latNum[i])

    print "points gotten"

    ## create the map
    m = Basemap(llcrnrlat=27,urcrnrlat=38.5,llcrnrlon=-118,urcrnrlon=-101,lat_ts=30)
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    m.drawmapboundary(fill_color=(0.5,0.5,0.5))
    m.fillcontinents(color="white")


    ## plot the jittered points, different colors/shapes for each desert
    #m.plot(nulx,nuly,'^',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(0.5,0.5,0.5),markersize=10)
    #m.plot(disx,disy,'o',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(0,1,0),markersize=10)
    #m.plot(locx,locy,'v',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=((160.0/255.0),(32.0/255.0),(240.0/255.0)),markersize=10)
    #m.plot(acrx,acry,'s',markeredgewidth='1.5',markeredgecolor="black",markerfacecolor=(0,0,1),markersize=10)

    ## save the figure and plot
    plt.savefig('C:/Users/Kaiya/Dropbox/Docs For Brian/THESIS/FIGURES/songtestBLANK.png',dpi=300, bbox_inches='tight')
    plt.show()
