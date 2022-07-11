import numpy as np
import pylab as pl
import glob


path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_3_map\\2022-06-03_17-17\\'
path_max = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_3_map\\2022-06-03_17-17\\max\\max.txt'
path_spectrum = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_3_map\\2022-06-03_17-17\\max\\spectrum\\'

def spectrum(x,y,name):
    
    pl.figure(names[n])
    pl.plot(x, y, "o-", linewidth = 2)
    pl.grid()
    pl.xlim(1520,1580)
    pl.ylim(-65,10)
    pl.show()
    pl.savefig(path_spectrum + names[n] + '.png')
    pl.close()
      
Stuff = glob.glob( path + '*.txt' )

max_x = np.array([])
max_y = np.array([])
names = np.array([])
Sum_P = np.array([])

n = 0
th = -30

for j in Stuff:
    
    x, y = np.genfromtxt( j, dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
    
    if np.max(y) > th: #Delete weak signals
      
        mask = y - np.max(y) > th
        xx = x[mask]
        yy = y[mask]
         
        if xx[-1] - xx[0] < 1: #Delete parasitic signals
            
            with open(j) as myfile:
                head = [next(myfile) for x in range(5)]
                  
            r = head[0].split('r:')[1].split("\n")[0]
            p = head[1].split('p:')[1].split("\n")[0]
            f = head[2].split('f:')[1].split("\n")[0]
            s = head[3].split('s:')[1].split("\n")[0]
            T = head[4].split('p:')[1].split("\n")[0]
        
            names = np.append( names, "r=" + r + "_p=" + p + "_f=" + f + "_s=" + s + "_T=" + T )
            max_x = np.append( max_x, x[np.where( y == np.max(y))[0][0]] )
            max_y = np.append( max_y, np.max(y) )
        
            # Calculate Power
            y_lin = 10**(y/10)*10**3 #mW
            Sum_P = np.append(Sum_P, np.trapz(y_lin)
            
            spectrum(x, y, names[n])
            n += 1
            print(n)        
        
        
Dict = np.zeros(names.size, dtype=[('var1', 'U34'), ('var2', float), ('var3', float), ('var4', float) ])
Dict['var1'] = names
Dict['var2'] = max_x
Dict['var3'] = max_y
Dict['var4'] = Sum_P

np.savetxt(path_max, Dict, fmt = "%1.34s;%1.3f;%1.7f;%1.7f;", header =
           "Name of file; Wavelength_max (nm); Intensity_max (dBm); Power_spectrum (mW) ")



