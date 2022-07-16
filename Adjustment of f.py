import numpy as np
import pylab as pl
import glob
from scipy import interpolate


path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_8_variation\\729\\pic\\1350\\'
path_r = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_6_main diag\\2022-06-08_17-35\\max\\Parameters\\Parameters.txt'
path_pic = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_8_variation\\729\\pic\\1350\\pic\\'

Stuff = glob.glob( path + '*.txt' )


def bandwidth(la, intensity,th):
    
    ind_max = np.where(intensity == np.max(intensity))[0][0]
    fl = interpolate.interp1d(intensity[ind_max-50:ind_max+1],la[ind_max-50:ind_max+1], kind='linear')
    fr = interpolate.interp1d(intensity[ind_max:ind_max+50],la[ind_max:ind_max+50], kind='linear')
    y_max = intensity[ind_max]
    width = fr(y_max-th) - fl(y_max-th)
    return width

#for parameters r and p
Stuff_r = glob.glob( path_r + '*.txt' )
r_par = np.array( 100*np.genfromtxt( path_r, dtype=float, unpack=True, usecols=[1], delimiter=';' ), dtype=int )
p_par = np.array( np.genfromtxt( path_r, dtype=float, unpack=True, usecols=[0], delimiter=';' ), dtype=int )


r = np.zeros(len(Stuff))
p = np.zeros(len(Stuff))
f = np.zeros(len(Stuff))

for j in range(len(Stuff)):
    
    with open(Stuff[j]) as myfile:
        head = [next(myfile) for x in range(10)] 
    # print(head)
    r[j] = float(head[1].split('r:')[1].split("\n")[0])
    p[j] = float(head[2].split('p:')[1].split("\n")[0])
    f[j] = float(head[3].split('f:')[1].split("\n")[0])
    print(j)

#%%

f_get = np.zeros(r_par.size)
width_3_get = np.zeros(r_par.size)
lamb_get = np.zeros(r_par.size)
Ints_get = np.zeros(r_par.size)
width_10_get = np.zeros(r_par.size)
width_20_get = np.zeros(r_par.size)
for k in range(r_par.size):
# for k in [117]:
    
    print("k = {0:d}/{1:d}".format(k, r_par.size-1))    
    
    a = np.where( r == r_par[k] )[0]
    b = np.where( p == p_par[k] )[0]
    i_r_p = np.asarray( [ x for x in a if x in b] )
    print(i_r_p)
    
    f_loc = f[( r == r_par[k] )&( p == p_par[k] )]
    delta = np.abs( f_loc - r_par[k] )
    i_f_par_l = np.where( delta == delta.min() )[0][0]
    f_par = f_loc[i_f_par_l]
    if k < 45:
        l = k
        i_f_glob = i_f_par_l + 15*l
    else:
        l = k - 45
        i_f_glob = i_f_par_l + 675 + 30*l

    #Spectrum for f ~ r and lambda_max
    x, y = np.genfromtxt( Stuff[i_f_glob], dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
    la_m = x[np.where( y == np.max(y) )[0][0]] #la_max of f ~ r
        
        
    lambs = np.zeros( i_r_p.size )
    width_3 = np.zeros( i_r_p.size )
    width_10 = np.zeros( i_r_p.size )
    width_20 = np.zeros( i_r_p.size )
    Ints = np.zeros( i_r_p.size )
    for i in range( len(i_r_p) ):
            
        x, y = np.genfromtxt( Stuff[int (i_r_p[i]) ], dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
                
        # th = 10
        #Removing of parasitic spectrums
        xx = x[y - np.max(y) > -30]
        yy = y[y - np.max(y) > -30]
     
        if xx[-1] - xx[0] < 1:
            
            
            # lambs[i] = x[np.where( y == np.max(y) )[0][0]]
            mask = ( np.max(y) - y ) < 10
            
            lambs[i] = np.sum(y[mask]*x[mask])/(np.sum(y[mask]))
            
            width_3[i] = bandwidth(x, y, 3)*1000 
            width_10[i] = bandwidth(x, y, 10)*1000 
            width_20[i] = bandwidth(x, y, 20)*1000 
            Ints[i] = y[y == np.max(y)]
            
    #Cleaning from zeros
    i_r_p_cl = i_r_p[lambs != 0]    
    lambs_cl = lambs[lambs != 0]
    width_3_cl = width_3[width_3 != 0]
    width_10_cl = width_10[width_10 != 0]
    width_20_cl = width_20[width_20 != 0]
    Ints_cl = Ints[Ints != 0]
    
    dl = abs( lambs_cl - la_m )
        
    lamb_n = lambs_cl[dl < 1.]
    Ints_n = Ints_cl[dl < 1.]
    i_n = i_r_p_cl[dl < 1.]
    f_n = f[i_n]
    width_3_n = width_3_cl[dl < 1.]
    width_10_n = width_10_cl[dl < 1.]
    width_20_n = width_20_cl[dl < 1.]
    # print(width_n)
    
    i_n = i_n[width_10_n == np.min(width_10_n)]
    width_3_get[k] = np.min(width_3_n)
    width_10_get[k] = np.min(width_10_n)
    width_20_get[k] = np.min(width_20_n)
    lamb_get[k] = lamb_n[width_10_n == np.min(width_10_n)]
    Ints_get[k] = Ints_n[width_10_n == np.min(width_10_n)]
    f_get[k] = f[i_n[0]]/100
        
    name = "r = " + str(r_par[k]/100) +";" + " p = " + str(p_par[k])+";" + " f = " + str(f_get[k])
    
    # pl.figure(name)
    # pl.title(name)
    # pl.plot(f_n/100, width_n, "o-")
    # pl.xlabel("f (mA)", fontsize = 20)
    # pl.ylim(0)
    # pl.ylabel("width (pm)", fontsize = 20)
    # pl.grid()
    # pl.show()
    # pl.savefig(path_pic + name + '.png')
    # pl.close()
    
pl.figure()
pl.plot(f_get, r_par/100, "o")
pl.plot(r_par/100, r_par/100, "o-")
pl.grid()

# np.savetxt(path + "Parameters_modified_sredvzv" + '.txt',
#             np.c_[p_par, r_par, f_get*100, lamb_get],
#             fmt="%1.0f;%1.0f;%1.0f;%1.3f;",
#             header = 'Phase; r (mA); f (mA); Central Wavelength (nm)' )
