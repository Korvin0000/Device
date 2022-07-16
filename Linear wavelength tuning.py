import numpy as np
import pylab as pl
from scipy import interpolate


path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_8_variation\\729\\pic\\1350\\Parameters_modified_sredvzv.txt'
path_interpol = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_8_variation\\729\\pic\\1350\\'

p_k, r_k, f_k = np.genfromtxt( path, dtype=int, unpack=True, usecols=[0,1,2], delimiter=';' )
la_k = np.genfromtxt( path, dtype=float, unpack=True, usecols=[3], delimiter=';' )

la_new = np.array([])
p_0 = np.where(p_k == 0)[0]

for i in np.arange(0,5):
    
    if i == 0:
        
        la_new = np.append(la_new, la_k[p_0[0]:p_0[1]])
        
    else:
        
        shelf = la_k[p_0[i]:p_0[i+1]]
        shelf_end = la_k[p_0[i]-1]
        la_new = np.append( la_new, shelf[shelf < shelf_end] )
        
r_new = np.zeros(la_new.size)   
f_new = np.zeros(la_new.size)
p_new = np.zeros(la_new.size)

for i in np.arange(la_new.size):
    
    r_new[i] = r_k[np.where(la_k == la_new[i])][0]
    f_new[i] = f_k[np.where(la_k == la_new[i])][0]
    p_new[i] = p_k[np.where(la_k == la_new[i])][0]
    

dla_new = la_new[0:-1] - la_new[1:]

la_new = la_new[0:-1][dla_new>0]

r_new = r_new[0:-1][dla_new>0]
p_new = p_new[0:-1][dla_new>0]
f_new = f_new[0:-1][dla_new>0]

r_in = interpolate.interp1d(la_new, r_new, kind='linear')
p_in = interpolate.interp1d(la_new, p_new, kind='linear')
f_in = interpolate.interp1d(la_new, f_new, kind='linear')

la_lin=np.linspace(np.max(la_new), np.min(la_new), 750)


p_mask= p_in(la_lin[0:-1]) - p_in(la_lin[1:])
la_lin=la_lin[:-1][p_mask<0]

pl.figure()
pl.title("Parameters for linear tuning obtained from modified parameters", fontsize = 20)
pl.plot(la_lin, r_in(la_lin)/100, "o", label = "r (mA)")
pl.plot(la_lin, f_in(la_lin)/100, "o", label = "f (mA)")
pl.plot(la_lin, p_in(la_lin)/100, "o", label = "p (mA)")
pl.xlabel("Wavelength (nm)", fontsize = 20)
pl.ylabel("Parameters", fontsize = 20)
pl.ylim(0)
pl.grid()
pl.legend(fontsize = 20)
