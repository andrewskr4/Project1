import glob
import numpy as np
import os.path


f = glob.glob('*.png')
g = glob.glob('*.npy')
l=0

for i in range(len(g)):
    aname = g[i].split('.')
    fname = str(aname[0]) + str('.') + str(aname[1])
    for j in range(len(f)):
        if os.path.isfile(str(fname) + str('.png')):
            l=l+1
        else:    
            print('rm ' + str(g[i]))
            #print('rm ' + str(fname) + str('.npy'))
            break
