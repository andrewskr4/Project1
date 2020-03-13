from astropy.io import fits
#import imageio
#from PIL import Image
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
import glob

f = glob.glob('*.fit')
bias = np.load("averagebias.npy")
print(len(f))
print(bias.shape)
print(bias.dtype)
all_data = np.empty((15, 1023, 1536))


#print(len(g))
for i in range(len(f)):
    
    hdul = fits.open(f[i])
    fname = f[i].split('.')
    figname = fname[0] + str('.png')
    pyname = fname[0] + str('.npy')
    #hdul.info()

    data = hdul[0].data
    data = data - bias
    all_data[i] = data
    
    #print(data.shape)
    #print(data.dtype.name)
    #plt.imshow(data)
    np.save(pyname, data) 
    #plt.savefig(figname,bbox_inches='tight', transparent=True,pad_inches=0)
    hdul.close()
    print(i)

flat = np.average(all_data, axis=0)
#print(all_data.shape)
#print(flat.shape())
np.save("averageflat.npy", flat)


