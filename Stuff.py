import numpy as np
import pylab as pl
import glob



path = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\2022-05-13_23-59\\'

path_max = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\2022-05-13_23-59\\max\\dict.txt'

Stuff = glob.glob( path + '*.txt' )

max_x = np.array([])
max_y = np.array([])
names = np.array([])

for j in Stuff[35:36]:
    
    x, y = np.genfromtxt( j, dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
    
    names = np.append(names, j.split("2022-05-13_23-59\\")[1].split(".txt")[0] )
    max_y = np.append(max_y, np.max(y))
    max_x = np.append(max_x, x[np.where( y == np.max(y))[0][0]])
    pl.plot(x, y, label = j.split("2022-05-13_23-59\\")[1].split(".txt")[0], linewidth = 2)
    
# Dict = np.zeros(names.size, dtype=[('var1', 'U28'), ('var2', float), ('var3', float) ])
# Dict['var1'] = names
# Dict['var2'] = max_x
# Dict['var3'] = max_y
# print(max_x)

# np.savetxt(path_max, Dict, fmt="%1s;%1.1f;%1.7f", header = "Name of file; Wavelength_max (nm); Intensity_max (dB)")




# print("Ampl_max =",np.max(y), "dB")
    # print("Wavelength_max =", x[np.where( y == np.max(y))[0][0]], "nm")

    
# pl.xlabel('Wavelength (nm)', fontsize = 13)
# pl.ylabel('Amlitude (dB)', fontsize = 13)    
# pl.legend()
# pl.grid()
# pl.show()
