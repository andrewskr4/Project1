##### This program creates bias and flat corrected numpy
##### arrays for each fits file. These files are then
##### analyzed further by getlightcurve.py and finally
##### plotlightcurve.py


from astropy.io import fits
#import imageio
#from PIL import Image
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
import glob

f = glob.glob('*.fit')

bias = np.load("../bias/averagebias.npy")
flat = np.load("../flat/averageflat.npy")
print(len(f))
print(bias.shape)
print(bias.dtype)



#print(len(g))
for i in range(len(f)):
    
    hdul = fits.open(f[i])
    fname = f[i].split('.')
    figname = fname[0] +str('.')+ fname[1] + str('.png')
    pyname = fname[0] +str('.')+ fname[1] + str('.npy')
    #hdul.info()

    data = hdul[0].data
    data = data - bias
    data = np.divide(data, flat)
    
    #print(data.shape)
    np.save(pyname, data) 
    hdul.close()
    #print(i)
