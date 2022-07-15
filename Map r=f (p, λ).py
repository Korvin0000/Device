import numpy as np
import pylab as pl
import glob
from scipy.ndimage.filters import gaussian_filter


path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_6_main diag\\2022-06-08_17-35\\max\\'
path_map = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_6_main diag\\2022-06-08_17-35\\max\\map\\'
path_try = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_6_main diag\\2022-06-08_17-35\\max\\try\\'
path_parameters = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_6_main diag\\2022-06-08_17-35\\max\\Parameters\\'

Stuff = glob.glob( path + '*.txt' )


for j in Stuff:
    
    x = np.genfromtxt( j, dtype=str, unpack=True, usecols=[0], delimiter=';', skip_header = 2 )
    y,z,d = np.genfromtxt( j, dtype = 'f8', unpack=True, usecols=[1,2,3], delimiter=';', skip_header = 2 )
    w = np.genfromtxt( j, dtype = float, unpack=True, usecols=[4], delimiter=';', skip_header = 2 )
    
r = np.zeros(x.size)
p = np.zeros(x.size)
f = np.zeros(x.size)
s = np.zeros(x.size)
T = np.zeros(x.size)


for i in range(x.size):
    
    r[i] = x[i].split('r=')[1].split("_p")[0]
    p[i] = x[i].split('p=')[1].split("_f")[0]
    f[i] = x[i].split('f=')[1].split("_s")[0]
    s[i] = x[i].split('s=')[1].split("_T")[0]
    T[i] = x[i].split('T=')[1]

#beginning of search the currents in the middle of the diagonals
y_first = np.array([])
y_second = np.array([])
y_third = np.array([])
y_fourth = np.array([])
y_fifth = np.array([])
y_sixth = np.array([])

r_first = np.array([])
r_second = np.array([])
r_third = np.array([])
r_fourth = np.array([])
r_fifth = np.array([])
r_sixth = np.array([])

for j in np.arange(0,702,24):
    
    r_f = np.array([])
    y_1 = np.array([])
    
    for i in np.where(p == j)[0]:
        
        r_f = np.append(r_f, r[i]/100)
        y_1 = np.append(y_1, y[i])
    
    
    name = "Phase = " + str(j)
    
    pl.figure(name)
    pl.title(name, fontsize = 20)
    pl.plot(r_f, y_1, "o-")
    pl.grid()
    pl.xlabel("r == f (mA)", fontsize = 16)
    pl.ylabel("Wavelength (nm)", fontsize = 16)
    pl.ylim(1556.545, 1561.323)
    pl.xlim(4.2, 33.06)
    pl.show()


    y_1 = y_1[r_f>4.31]
    r_f = r_f[r_f>4.31]
    dy = y_1[1:] - y_1[:-1]
    dy = dy+0.1
    dy[dy<0]=0
    
    p_ = np.where(dy==0)[0]+1
   
    
    if j == 0 or j == 24:
        
        pl.plot(r_f[p_[0]:p_[1]],y_1[p_[0]:p_[1]], linewidth = 4)
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:p_[6]],y_1[p_[5]:p_[6]], linewidth = 4)
        
        
        Dela_0 = np.abs(y_1[p_[0]:p_[1]]-y_1[p_[0]:p_[1]].mean())
        y_av_0 = y_1[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        r_av_0 = r_f[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:p_[6]]-y_1[p_[5]:p_[6]].mean())
        y_av_5 = y_1[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_0)
        y_second = np.append(y_second, y_av_1)
        y_third = np.append(y_third, y_av_2)
        y_fourth = np.append(y_fourth, y_av_3)
        y_fifth = np.append(y_fifth, y_av_4)
        y_sixth = np.append(y_sixth, y_av_5)
        
        r_first = np.append(r_first, r_av_0)
        r_second = np.append(r_second, r_av_1)
        r_third = np.append(r_third, r_av_2)
        r_fourth = np.append(r_fourth, r_av_3)
        r_fifth = np.append(r_fifth, r_av_4)
        r_sixth = np.append(r_sixth, r_av_5)
        
           
    if j == 48 or j == 72:
        
        pl.plot(r_f[p_[0]:p_[1]],y_1[p_[0]:p_[1]], linewidth = 4)
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:],y_1[p_[5]:], linewidth = 4)
        
        
        Dela_0 = np.abs(y_1[p_[0]:p_[1]]-y_1[p_[0]:p_[1]].mean())
        y_av_0 = y_1[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        r_av_0 = r_f[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:]-y_1[p_[5]:].mean())
        y_av_5 = y_1[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_0)
        y_second = np.append(y_second, y_av_1)
        y_third = np.append(y_third, y_av_2)
        y_fourth = np.append(y_fourth, y_av_3)
        y_fifth = np.append(y_fifth, y_av_4)
        y_sixth = np.append(y_sixth, y_av_5)
        
        r_first = np.append(r_first, r_av_0)
        r_second = np.append(r_second, r_av_1)
        r_third = np.append(r_third, r_av_2)
        r_fourth = np.append(r_fourth, r_av_3)
        r_fifth = np.append(r_fifth, r_av_4)
        r_sixth = np.append(r_sixth, r_av_5)
        
    if  j == 96 or j == 120 or j == 144 or j == 168 or j == 192:
        
        pl.plot(r_f[p_[0]:p_[1]],y_1[p_[0]:p_[1]], linewidth = 4)
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        
        
        Dela_0 = np.abs(y_1[p_[0]:p_[1]]-y_1[p_[0]:p_[1]].mean())
        y_av_0 = y_1[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        r_av_0 = r_f[p_[0]:p_[1]][np.where(Dela_0 == Dela_0.min())]
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        y_first = np.append(y_first, y_av_0)
        y_second = np.append(y_second, y_av_1)
        y_third = np.append(y_third, y_av_2)
        y_fourth = np.append(y_fourth, y_av_3)
        y_fifth = np.append(y_fifth, y_av_4)
       
        
        r_first = np.append(r_first, r_av_0)
        r_second = np.append(r_second, r_av_1)
        r_third = np.append(r_third, r_av_2)
        r_fourth = np.append(r_fourth, r_av_3)
        r_fifth = np.append(r_fifth, r_av_4)
     
   
    if j == 216 or j == 240 or j == 264 or j == 288 or j == 312 or j == 336 or j == 360 or j == 384 or j == 408 or j == 432:

        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:p_[6]],y_1[p_[5]:p_[6]], linewidth = 4)
        
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:p_[6]]-y_1[p_[5]:p_[6]].mean())
        y_av_5 = y_1[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_1)
        y_second = np.append(y_second, y_av_2)
        y_third = np.append(y_third, y_av_3)
        y_fourth = np.append(y_fourth, y_av_4)
        y_fifth = np.append(y_fifth, y_av_5)
        
        r_first = np.append(r_first, r_av_1)
        r_second = np.append(r_second, r_av_2)
        r_third = np.append(r_third, r_av_3)
        r_fourth = np.append(r_fourth, r_av_4)
        r_fifth = np.append(r_fifth, r_av_5)
        
        
    if j == 456:
   
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:],y_1[p_[5]:], linewidth = 4)
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:]-y_1[p_[5]:].mean())
        y_av_5 = y_1[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_1)
        y_second = np.append(y_second, y_av_2)
        y_third = np.append(y_third, y_av_3)
        y_fourth = np.append(y_fourth, y_av_4)
        y_fifth = np.append(y_fifth, y_av_5)
        
        r_first = np.append(r_first, r_av_1)
        r_second = np.append(r_second, r_av_2)
        r_third = np.append(r_third, r_av_3)
        r_fourth = np.append(r_fourth, r_av_4)
        r_fifth = np.append(r_fifth, r_av_5)
 
    if j == 480:
        
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:p_[6]],y_1[p_[5]:p_[6]], linewidth = 4)
        pl.plot(r_f[p_[6]:],y_1[p_[6]:], linewidth = 4)
        
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:p_[6]]-y_1[p_[5]:p_[6]].mean())
        y_av_5 = y_1[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        
        
        Dela_6 = np.abs(y_1[p_[6]:]-y_1[p_[6]:].mean())
        y_av_6 = y_1[p_[6]:][np.where(Dela_6 == Dela_6.min())]
        r_av_6 = r_f[p_[6]:][np.where(Dela_6 == Dela_6.min())]
        
        y_first = np.append(y_first, y_av_2)
        y_second = np.append(y_second, y_av_3)
        y_third = np.append(y_third, y_av_4)
        y_fourth = np.append(y_fourth, y_av_5)
        y_fifth = np.append(y_fifth, y_av_6)
        
        r_first = np.append(r_first, r_av_2)
        r_second = np.append(r_second, r_av_3)
        r_third = np.append(r_third, r_av_4)
        r_fourth = np.append(r_fourth, r_av_5)
        r_fifth = np.append(r_fifth, r_av_6)
        
        
    
    if j == 504 or j == 528 or j == 552 or j == 576 or j == 600:
        
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:],y_1[p_[5]:], linewidth = 4)
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:]-y_1[p_[5]:].mean())
        y_av_5 = y_1[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_1)
        y_second = np.append(y_second, y_av_2)
        y_third = np.append(y_third, y_av_3)
        y_fourth = np.append(y_fourth, y_av_4)
        y_fifth = np.append(y_fifth, y_av_5)
        
        r_first = np.append(r_first, r_av_1)
        r_second = np.append(r_second, r_av_2)
        r_third = np.append(r_third, r_av_3)
        r_fourth = np.append(r_fourth, r_av_4)
        r_fifth = np.append(r_fifth, r_av_5)
        
    
    if j == 624 or j == 648 or j == 672:
        
        pl.plot(r_f[p_[1]:p_[2]],y_1[p_[1]:p_[2]], linewidth = 4)
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        
        Dela_1 = np.abs(y_1[p_[1]:p_[2]]-y_1[p_[1]:p_[2]].mean())
        y_av_1 = y_1[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        r_av_1 = r_f[p_[1]:p_[2]][np.where(Dela_1 == Dela_1.min())]
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        y_first = np.append(y_first, y_av_1)
        y_second = np.append(y_second, y_av_2)
        y_third = np.append(y_third, y_av_3)
        y_fourth = np.append(y_fourth, y_av_4)
                
        r_first = np.append(r_first, r_av_1)
        r_second = np.append(r_second, r_av_2)
        r_third = np.append(r_third, r_av_3)
        r_fourth = np.append(r_fourth, r_av_4)
      
           
    
    if j == 696:
        
        
        pl.plot(r_f[p_[2]:p_[3]],y_1[p_[2]:p_[3]], linewidth = 4)
        pl.plot(r_f[p_[3]:p_[4]],y_1[p_[3]:p_[4]], linewidth = 4)
        pl.plot(r_f[p_[4]:p_[5]],y_1[p_[4]:p_[5]], linewidth = 4)
        pl.plot(r_f[p_[5]:p_[6]],y_1[p_[5]:p_[6]], linewidth = 4)
        
        
        Dela_2 = np.abs(y_1[p_[2]:p_[3]]-y_1[p_[2]:p_[3]].mean())
        y_av_2 = y_1[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        r_av_2 = r_f[p_[2]:p_[3]][np.where(Dela_2 == Dela_2.min())]
        
        Dela_3 = np.abs(y_1[p_[3]:p_[4]]-y_1[p_[3]:p_[4]].mean())
        y_av_3 = y_1[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        r_av_3 = r_f[p_[3]:p_[4]][np.where(Dela_3 == Dela_3.min())]
        
        Dela_4 = np.abs(y_1[p_[4]:p_[5]]-y_1[p_[4]:p_[5]].mean())
        y_av_4 = y_1[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        r_av_4 = r_f[p_[4]:p_[5]][np.where(Dela_4 == Dela_4.min())]
        
        Dela_5 = np.abs(y_1[p_[5]:p_[6]]-y_1[p_[5]:p_[6]].mean())
        y_av_5 = y_1[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        r_av_5 = r_f[p_[5]:p_[6]][np.where(Dela_5 == Dela_5.min())]
        
        y_first = np.append(y_first, y_av_2)
        y_second = np.append(y_second, y_av_3)
        y_third = np.append(y_third, y_av_4)
        y_fourth = np.append(y_fourth, y_av_5)
                
        r_first = np.append(r_first, r_av_2)
        r_second = np.append(r_second, r_av_3)
        r_third = np.append(r_third, r_av_4)
        r_fourth = np.append(r_fourth, r_av_5)
        


phase = np.arange(0,702,24)

pl.figure('Map r==f(p, Lambda)')
pl.title("Map r==f (p, Lambda)", fontsize = 20)
pl.tricontour(p, r/100, y, 200, vmin = 1556, vmax = 1561.26, cmap = 'nipy_spectral', levels = 1000)
pl.xlabel("p", fontsize = 20)
pl.ylim(5,30)
pl.ylabel("r = f (mA)", fontsize = 20)
pl.colorbar()

pl.plot(phase, r_first, "o-")
pl.plot(phase, r_second, "o-")
pl.plot(phase, r_third[:-1], "o-")
pl.plot(phase, r_fourth, "o-")
pl.plot(phase[:-3], r_fifth, "o-")
pl.plot(phase[:4], r_sixth, "o-")
pl.show()

pl.figure('Wavelength')
pl.plot(np.concatenate((y_first, y_second, y_third[:-1], y_fourth, y_fifth, y_sixth),
                        axis = None), "o-")
pl.xlabel("Index (N)", fontsize = 20)
pl.ylabel("Wavelength (nm)", fontsize = 20)
pl.grid()
pl.show()

La = np.concatenate((y_first, y_second, y_third[:-1], y_fourth, y_fifth, y_sixth), axis = None)
r__f = np.concatenate((r_first, r_second, r_third[:-1], r_fourth, r_fifth, r_sixth), axis = None)
ph = np.concatenate((phase, phase, phase, phase, phase[:-3], phase[:4]), axis = None)

np.savetxt(path_parameters + "Parameters" + '.txt', np.c_[ph, r__f, La], fmt="%1.0f;%1.2f;%1.3f;", header = 'Phase; r = f (mA); Wavelength (nm)' )
