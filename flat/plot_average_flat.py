import numpy as np
import matplotlib.pyplot as plt


data = np.load('averageflat.npy')
figname = str('averageflat.png')
plt.imshow(data)
plt.savefig(figname,bbox_inches='tight', transparent=True,pad_inches=0)



