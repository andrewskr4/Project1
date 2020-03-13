import glob

f = glob.glob('*npy.png')

for i in range(len(f)):
    fname = f[i].split('n')
    figname = fname[0] + str('.png')
    print("mv "+str(f[i])+ " " + str(figname))
