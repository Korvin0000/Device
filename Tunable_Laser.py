import numpy as np
import pylab as pl
import glob

#%%
path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\2022-05-13_23-59\\'

path_Power = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\2022-05-13_23-59\\Power\\Power.txt'

Stuff = glob.glob( path + '*.txt' )

max_x = np.array([])
max_y = np.array([])
names = np.array([])
Sum_P = np.array([])

max_x_p = np.array([])
max_y_p = np.array([])

for j in Stuff:
   
    x, y = np.genfromtxt( j, dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
    
    if np.max(y) > -80: #Delete noise
    
        names = np.append(names, j.split("2022-05-13_23-59\\")[1].split(".txt")[0] )
        max_y = np.append(max_y, np.max(y))
        max_x = np.append(max_x, x[np.where( y == np.max(y))[0][0]])
         
        x_poly = np.array([])
        y_poly = np.array([])
        
        for i in range( np.where( y == np.max(y))[0][0] - 2, np.where( y == np.max(y))[0][0] + 3):
 
            y_poly = np.append(y_poly, y[i])
            x_poly = np.append(x_poly, x[i])
            
        poly = np.polyfit(x_poly, y_poly, 2)
        poly_der = np.polyder(poly)
        
        la_min = np.roots(poly_der) # max x after poly
        p = np.poly1d(poly) # max y after poly
        max_x_p = np.append( max_x_p, la_min )
        max_y_p = np.append( max_y_p, p(la_min) )
 
        # Calculate Power
        y_lin = 10**(y/10)*10**6 #mcW
        Sum_P = np.append(Sum_P, np.trapz(y_lin))
    
#         pl.plot(x, y, "o-", label = str(np.trapz(y_lin))+" mcW",  linewidth = 2)
#         pl.plot(x_poly, p(x_poly), "o-")
#         pl.xlim(1450,1650)
#         pl.ylim(-210,-50)
    
pl.plot(max_x_p - max_x)
pl.xlim(0,3806)
pl.legend()
pl.grid()
pl.show()
pl.figure()
pl.plot(max_y_p - max_y)
pl.legend()
pl.grid()
pl.show()

# Dict = np.zeros(names.size, dtype=[('var1', 'U28'), ('var2', float), ('var3', float), ('var4', float) ])
# Dict['var1'] = names
# Dict['var2'] = max_x_p
# Dict['var3'] = max_y_p
# Dict['var4'] = Sum_P
# print(max_x)

# np.savetxt(path_Power, Dict, fmt="%1s;%1.1f;%1.7f;%1.7f;", header = "Name of file; Wavelength_max (nm); Intensity_max (dB); Sum_P (mcW)")
# %%


path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\2022-05-13_23-59\\Power\\'

Stuff = glob.glob( path + '*.txt' )


for j in Stuff:
    
    x = np.genfromtxt( j, dtype=str, unpack=True, usecols=[0], delimiter=';', skip_header = 2 )
    y,z,d = np.genfromtxt( j, dtype = 'f8', unpack=True, usecols=[1,2,3], delimiter=';', skip_header = 2 )

    
r = np.zeros(x.size)
p = np.zeros(x.size)
f = np.zeros(x.size)
s = np.zeros(x.size)


for i in range(x.size):
    
    r[i] = x[i].split('r=')[1].split("_p")[0]
    p[i] = x[i].split('p=')[1].split("_f")[0]
    f[i] = x[i].split('f=')[1].split("_s")[0]
    s[i] = x[i].split('s=')[1]


r1 = np.array([])
f1 = np.array([])
y1 = np.array([])

z1 = np.array([])
x1 = np.array([])
d1 = np.array([])

for i in np.where(p==0)[0]:
    
    r1 = np.append(r1, r[i])
    f1 = np.append(f1, f[i])
    y1 = np.append(y1, y[i])
    
    x1 = np.append(x1, x[i])
    z1 = np.append(z1, z[i])
    d1 = np.append(d1, d[i])

# f2 = f1[z1>-80]
# r2 = r1[z1>-80]
# y2 = y1[z1>-80]
# d2 = d1[z1>-80]

pl.figure('Map')
pl.tricontourf(f1,r1,10*np.log(d1/10**6), 200, cmap = 'gnuplot_r', levels = 1200)
pl.colorbar()
pl.show()





