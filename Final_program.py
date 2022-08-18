import numpy as np
import pylab as pl
import glob
from scipy import interpolate

#Calculation of map f(p, la)
path = 'C:\\Users\\Nikolay\\Desktop\\FOS\\New_map\\Exp_1\\2022-08-07_18-40\\'
path_max = 'C:\\Users\\Nikolay\\Desktop\\FOS\\New_map\\Exp_1\\'

p = np.array([])
r = np.array([])
f = np.array([])
la = np.array([])

def Search_max(x, y, th, N):   
    
    global p, r, f, la
    xx = x[y - np.max(y) > th] #Selection (Only single mode regime)
    if xx[-1] - xx[0] < 1:
        with open(N) as myfile:
            head = [next(myfile) for k in range(5)]                
        #Parameters for each spectum
        r = np.append(r, int(head[1].split('r:')[1].split("\n")[0]))
        p = np.append(p, int(head[2].split('p:')[1].split("\n")[0]))
        f = np.append(f, int(head[3].split('f:')[1].split("\n")[0]))
        #la_max
        la = np.append(la, x[np.where( y == np.max(y))[0][0]])

def Map_Plot(p, f, la):
    
    pl.figure('Map f (p, λ)')
    pl.title("Map f (p, λ)", fontsize = 20)
    pl.tricontour(p, f, la, 200, cmap = 'nipy_spectral', levels = 250)
    pl.xlabel("p", fontsize = 20)
    pl.ylabel("f (mA)", fontsize = 20)
    pl.colorbar()

#Main block
try:
    
    data = np.load(path_max +'max.npz')
    p = data[data.files[0]]
    r = data[data.files[1]]
    f = data[data.files[2]]
    la = data[data.files[3]]

except:
    
    n = 0
    Stuff = glob.glob( path + '*.txt' )
    for j in Stuff:
        x, y = np.genfromtxt( j, dtype=float, unpack=True, usecols=[0, 1], delimiter=';' )
        Search_max(x, y, -30, j)
        n += 1
        print(n)    
    
    np.savez(path_max +'max.npz', p = p, r = r, f = f, la = la)

# Map_Plot(p, f, la)
# Search of the middle on the map f(p, la)

arr = []
arr_f = []
arr_p = []

def Der_la(la_1, height):
    
    dla = la_1[1:] - la_1[:-1]
    dla_2 = np.array(dla)
    dla_2[np.abs(dla_2) < height]=0
    dla_2[np.abs(dla_2) > height]=1
    return dla_2

def Slice_Plot(N, f_1, la_1, la_3, f_3):
    
    name = "Phase = " + str(N)
    pl.figure(name)
    pl.title(name, fontsize = 20)
    pl.plot(f_1, la_1, "ko-")
    pl.grid()
    pl.xlim(0)
    pl.xlabel("f (mA)", fontsize = 16)
    pl.ylabel("Wavelength (nm)", fontsize = 16)
    for i in range(len(la_3)):
        pl.plot(f_3[i],la_3[i], linewidth = 4)
    pl.show()

def Wavelength_Tuning_Plot(la_new):
   
    pl.figure("Wavelength tuning")
    pl.plot(la_new, "o-")
    pl.xlabel("Index (N)", fontsize = 20)
    pl.ylabel("Wavelength (nm)", fontsize = 20)
    pl.grid()
    pl.show()
    
min_shelve_size = 4

#Passing through the vertical slices of map
Phases = np.arange(0,702,24)
for j in Phases:
    
    f_1 = np.array([])
    la_1 = np.array([])
    for i in np.where(p == j)[0]:
        
        f_1 = np.append(f_1, f[i])
        la_1 = np.append(la_1, la[i])
        
    #To recognize the shelves between derivative jumps  
    f_2 = np.array_split(f_1, np.where( Der_la(la_1, 0.1) == 1 )[0]+1)
    la_2 = np.array_split(la_1, np.where( Der_la(la_1, 0.1) == 1 )[0]+1)
    
    #Lists for the shelves that will consist of np.arrays
    la_3 = []
    f_3 = []
    la_max = []
    f_max = []

    #To choose the certain shelves
    for i in range(len(la_2)):
        if (la_2[i].size > min_shelve_size):
            la_3.append(la_2[i])
            f_3.append(f_2[i])
            
    #Middle        
    for i in range(len(la_3)): 
        Dela = np.abs( la_3[i] - la_3[i].mean() ) #Choose exp mean
        la_max.append(la_3[i][ np.where( Dela == Dela.min() ) ][0])
        f_max.append(f_3[i][ np.where( Dela == Dela.min() ) ][0])
    
    Slice_Plot(j, f_1, la_1, la_3, f_3)
    
    if j == 0:
        for i in range(len(la_max)):
            
            arr.append(np.array([la_max[i]]))
            arr_f.append(np.array([f_max[i]]))
            arr_p.append(np.array([j]))
    else: 
        if np.abs(la_max[0] - arr[0][-1]) > .2:
            
            print(j)
            arr.insert(0, np.array([]))
            arr_f.insert(0, np.array([]))
            arr_p.insert(0, np.array([]))
            
        for i in range(len(la_max)):
                
            arr[i] = np.append(arr[i], la_max[i])
            arr_f[i] = np.append(arr_f[i], f_max[i])
            arr_p[i] = np.append(arr_p[i], j)
  
Map_Plot(p,f,la)
for i in range(len(arr)):
    pl.plot(arr_p[i],arr_f[i],'o-', markersize = 10, linewidth = 5)
    
la_new = np.concatenate( (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9]), axis = None)
Wavelength_Tuning_Plot(la_new)

# p, f, arr_la = la_new
#Defenition of r_new for got f_new
path_r_f = 'C:\\Users\\Nikolay\\Desktop\\Stuff\\Exp_15_Phase_variation_for_all_diag\\Main diag. Yellow from new map..txt'
r_map, f_map = np.genfromtxt( path_r_f, dtype=int, unpack=True, usecols = [ 0, 1 ], delimiter=';', skip_header = 1 )
#interpolation
r_in = interpolate.interp1d(f_map, r_map, kind='linear')
f_in = np.arange(min(f_map)+1,max(f_map)+1, 1)
# pl.plot(f_map, r_map, "o-", markersize = 10)
# pl.plot(f_in, r_in(f_in), "o-", markersize = 6)
# pl.grid()

#f_new = arr_f
p_new = np.concatenate( (arr_p[0], arr_p[1], arr_p[2], arr_p[3], arr_p[4], arr_p[5], arr_p[6], arr_p[7], arr_p[8], arr_p[9]), axis = None).astype(int)
# p_new = arr_p
f_new = np.concatenate( (arr_f[0], arr_f[1], arr_f[2], arr_f[3], arr_f[4], arr_f[5], arr_f[6], arr_f[7], arr_f[8], arr_f[9]), axis = None).astype(int)
#r_new
ind = np.zeros(f_new.size)
for i in range(f_new.size):
    if f_new[i] in f_in: 
        ind[i] = np.where(f_in == f_new[i])[0][0]
ind = np.array(ind, dtype = int)
r_new = np.round((r_in(f_in))[ind]).astype(int)
# np.savez(path_max +'Parameters_1.npz', p = p_new, r = r_new, f = f_new, la = la_new)

#Create linear tuning
p_k = p_new
r_k = r_new
f_k = f_new
la_k = la_new

# p_k = p_k[:147]
# r_k = r_k[:147]
# f_k = f_k[:147]
# la_k = la_k[:147]

la_new = np.array([])

la_ = np.array_split(la_k, np.where(p_k == 0)[0])
p_ = np.array_split(p_k, np.where(p_k == 0)[0])
r_ = np.array_split(r_k, np.where(p_k == 0)[0]) 
f_ = np.array_split(f_k, np.where(p_k == 0)[0])

la_ = la_[1:]
p_ = p_[1:]
r_ = r_[1:]
f_ = f_[1:]

for i in range(len(la_)):
    
    # pl.plot(la_[i], "o-")

    dla_ = la_[i][0:-1] - la_[i][1:]

    la_[i] = la_[i][0:-1][dla_>0 ]
    p_[i] = p_[i][0:-1][dla_>0 ]
    r_[i] = r_[i][0:-1][dla_>0 ]
    f_[i] = f_[i][0:-1][dla_>0 ]
    
    la_new = np.append(la_new, la_[i])

#Interpolation
la_lin=np.linspace(np.max(la_new), np.min(la_new), 150)

#for each section
la_lin_ = [] 
r_in_ = []
p_in_ = []
f_in_ = []

for i in range(len(la_)):
    
    lat = la_lin[ (la_lin <= la_[i][0]) & (la_lin >= la_[i][-1]) ]
    la_lin_.append( lat )
    # pl.plot(la_lin_[i])
    
    r_in = interpolate.interp1d(la_[i], r_[i], kind='linear') 
    r_in_.append( r_in(la_lin_[i]) )
    p_in = interpolate.interp1d(la_[i], p_[i], kind='linear') 
    p_in_.append( p_in(la_lin_[i]) )
    f_in = interpolate.interp1d(la_[i], f_[i], kind='linear')
    f_in_.append( f_in(la_lin_[i]) )

# pl.figure()
# for i in range(len(la_)):
    
#     pl.plot(la_[i], r_[i],'o')
#     pl.plot(la_lin_[i], r_in_[i])
    
#     pl.plot(la_[i], f_[i],'o')
#     pl.plot(la_lin_[i], f_in_[i])
    
#     pl.plot(la_[i], p_[i],'o')
#     pl.plot(la_lin_[i], p_in_[i])

r_new = np.array([])
f_new = np.array([])
p_new = np.array([])


for i in range(len(la_)-1):
    
    mid = (la_lin_[i][-1]+la_lin_[i+1][0])/2
    
    r_in_[i] = r_in_[i][la_lin_[i]>=mid]
    r_in_[i+1] = r_in_[i+1][la_lin_[i+1]<mid]
    
    f_in_[i] = f_in_[i][la_lin_[i]>=mid]
    f_in_[i+1] = f_in_[i+1][la_lin_[i+1]<mid]
    
    p_in_[i] = p_in_[i][la_lin_[i]>=mid]
    p_in_[i+1] = p_in_[i+1][la_lin_[i+1]<mid]
    
    la_lin_[i] = la_lin_[i][la_lin_[i]>=mid]
    la_lin_[i+1] = la_lin_[i+1][la_lin_[i+1]<mid]
    

pl.figure()
for i in range(len(la_)):
    
    r_new = np.append(r_new, r_in_[i])
    f_new = np.append(f_new, f_in_[i])
    p_new = np.append(p_new, p_in_[i])

pl.plot(la_lin, r_new, "o",  label = "r")
pl.plot(la_lin, f_new, "o",  label = "f")
pl.plot(la_lin, p_new, "o",  label = "p")
pl.legend()
pl.grid()

path_interpol = 'C:\\Users\\Nikolay\\Desktop\\FOS\\Tunings\\1st\\Parameters_Linear_tuning_1560.5_1557.2.txt'

# np.savetxt(path_interpol, np.c_[p_new, r_new, f_new], fmt="%1.0f;%1.0f;%1.0f;",
#             header = "p; r; f;")
