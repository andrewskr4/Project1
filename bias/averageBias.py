from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import glob

f = glob.glob('*.fit')

dat= np.empty((15, 1023, 1536))

for i in range(len(f)):
    hdul = fits.open(f[i])
    #hdul.info()
    dat[i] = hdul[0].data
    print(hdul[0].data.shape)
    hdul.close()
    print(i)

dat.shape
bias = np.average(dat, axis=0)
print(bias)
np.save("averagebias.npy", bias)
plt.imshow(bias)
figname = 'averagebias.png'
plt.savefig(figname,bbox_inches='tight', transparent=True,pad_inches=0)
plt.show()
    
