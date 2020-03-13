
########    In order for this and plotlightcurve.py to work properly
########    be sure to use the syntax:
########
########         python getlightcurve.py -> fluxes.txt
########
########    then run: python plotlightcurve.py to plot the light curve
########
########    For every rerun of getlightcurve.py you must remove the
########    original fluxes.txt
import numpy as np
import matplotlib.pyplot as plt
import glob
import multiprocessing as mp
from joblib import Parallel, delayed
import matplotlib.patches as patches

#run on multiple cores so the plots can be produced faster
num_cores = mp.cpu_count()

xmin = 600
ymin = 400
xmax = 0
ymax = 0
controlxmax = 0
controlymax = 0
prevflux = 0

f = glob.glob('*.npy')
r = 2

#function to plot all the fits files and
#print out 3 columns corresponding to the file number (proxy for time),
#the non-airmass corrected flux from out star, and the flux from the
#control star.
def plot(i):
    flux = 0
    prevflux = 0
    controlflux = 0

    y_index = np.array([])
    x_index = np.array([])
    controly_index = np.array([])
    controlx_index = np.array([])
    
    maximum = 0
    controlmax = 0
    fig,ax = plt.subplots(1)
    #rect = patches.Rectangle((xmin, ymin), 200, 100, linewidth=1, edgecolor='r',facecolor='none')
    data = np.load(f[i])

    #for each image, get the position of our star.
    #The range for each loop corresponds to a rectangle
    #that encapsulates the entire path of the
    #star as it moves across the images.
    for y in range(400,500):
        for x in range(600,800):
            if (data[y,x] > maximum):
                maximum = data[y,x]
                xmax = x
                ymax = y
                
    #for each image, get position of control star
    for y in range(600,800):
        for x in range(700,900):
            if (data[y,x] > controlmax):
                controlmax = data[y,x]
                controlxmax = x
                controlymax = y

    #collect flux in a circle around our star
    for y in range  (400, 500):
        for x in range(600,800):
            if ((x - xmax)**2 + (y-ymax)**2)<r**2:
                y_index = np.append(y_index, y)
                x_index = np.append(x_index, x)

                
    #collect flux around control star
    for y in range  (600, 800):
        for x in range(700,900):
            if ((x - controlxmax)**2 + (y-controlymax)**2)<r**2:
                controly_index = np.append(controly_index, y)
                controlx_index = np.append(controlx_index, x)

    #Sum flux from points in the circle around our star
    for j in range(len(x_index)):
        y = int(y_index[j])
        x = int(x_index[j])
        flux = flux + data[y,x]

    #Sum flux from points in the circle around the
    #control star
    for j in range(len(controlx_index)):
        y = int(controly_index[j])
        x = int(controlx_index[j])
        controlflux = controlflux + data[y,x]

    #the following line creates a red circle
    #where the alorithm thinks our star or the control star is depending
    #on which x and y coordinates you give it. (controlxmax, controlymax)
    #or (xmax, ymax)
    circle = plt.Circle((controlxmax, controlymax), radius=6, fc='r')
    fname = f[i].split('.')
    figname = fname[0] +str('.')+ fname[1] + str('.png')
    
    ax.imshow(data)
    #ax.add_patch(rect)

    #uncomment the following line to draw the circle
    ax.add_patch(circle)
    plt.savefig(figname,bbox_inches='tight', transparent=True,pad_inches=0)
    
    #get the fits file number and print out the 3 columns
    numName = fname[1].split('s')
    t = int(numName[2])
    print(str(t) + ' ' + str(flux) + ' ' + str(controlflux))
  
    return 1

out = Parallel(n_jobs=num_cores)(delayed(plot)(i) for i in range(len(f)))

