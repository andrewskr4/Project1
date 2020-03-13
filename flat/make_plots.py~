import numpy as np
import matplotlib.pyplot as plt
import glob
import multiprocessing as mp
from joblib import Parallel, delayed

num_cores = mp.cpu_count()

f = glob.glob('*.npy')

def plot(i):
    data = np.load(f[i])
    fname = f[i].split('.')
    figname = fname[0] +str('.')+ fname[1] + str('.png')
    #print(data.shape)
    plt.imshow(data)
    plt.savefig(figname,bbox_inches='tight', transparent=True,pad_inches=0)
    print(i)
    return 1
    
out = Parallel(n_jobs=num_cores)(delayed(plot)(i) for i in range(len(f)))


