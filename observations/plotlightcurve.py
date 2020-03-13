######### Plots the data from getlightcurve.py
######### after correcting the flux from our
######### star for airmass changes using a
######### control star.


import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

x = np.array([])
y = np.array([])
control = np.array([])

#read in times and fluxes of our star and control star
#from text file
with open('fluxes.txt') as f:
    for line in f:
        row = line.split()
        x = np.append(x, float(row[0]))
        y = np.append(y, float(row[1]))
        control = np.append(control, float(row[2]))

#sort images in time to allow for airmass correction (next loop)
combined = np.vstack((x,y,control)).T
combined = combined[combined[:,0].argsort()]

#get the difference in the flux from the control star
#between this and the previous image
for i in range(len(x)):
    if i==0:
        prevcontrol = combined[i][2]
    else:
        prevcontorl = combined[i-1][2]
    fluxdiff = combined[i][1] - prevcontrol


    #correct flux form our star but adding the difference in flux
    # of the control star
    combined[i][1] = combined[i][1] + fluxdiff

#plot light curve
plt.plot(combined[:,0],combined[:,1], marker='o', linestyle='None')
plt.show()
