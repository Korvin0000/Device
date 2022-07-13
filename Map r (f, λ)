import numpy as np
import pylab as pl
import glob

path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_3_map\\2022-06-03_17-17\\max\\'


Stuff = glob.glob( path + '*.txt' )

for j in Stuff:
    
    x = np.genfromtxt( j, dtype=str, unpack=True, usecols=[0], delimiter=';', skip_header = 2 )
    la = np.genfromtxt( j, dtype = 'f8', unpack=True, usecols=[1], delimiter=';', skip_header = 2 )


r = np.zeros(x.size)
f = np.zeros(x.size)
for i in range(x.size):
    
    r[i] = x[i].split('r=')[1].split("_p")[0]
    f[i] = x[i].split('f=')[1].split("_s")[0]

f = f/100
r = r/100


pl.figure('Map r (f, λ)')
pl.title("Map r (f, λ)", fontsize = 20)
pl.tricontour(f,r, la, 200, cmap = 'nipy_spectral', levels = 1000)
pl.xlim(0)
pl.ylim(4.5)
pl.xlabel("f (mA)", fontsize = 20)
pl.ylabel("r (mA)", fontsize = 20)
pl.colorbar()
pl.show()
