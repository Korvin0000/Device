import optelems3 as oe #return the position of cursor to the console
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

pl.figure('Map with diagonal currents')
pl.title("Map with diagonal currents", fontsize = 20)
pl.tricontour(f,r, la, 200, cmap = 'nipy_spectral', levels = 1000)
pl.ylim(4.5)
pl.xlabel("f (mA)", fontsize = 20)
pl.ylabel("r (mA)", fontsize = 20)
pl.colorbar()
oe.CoordsToConsol();
oe.FormatCoords();

# the most left
X_high = np.array([6.040866702e+00, 5.346879250e+00, 3.894808007e+00, 2.597733132e+00, 1.675912624e+00, 6.643573755e-01, 1.993682695e-01  ])
Y_high = np.array([2.769632390e+01, 2.541751016e+01, 2.128085221e+01, 1.658329150e+01, 1.272708495e+01, 8.415144890e+00, 5.820969571e+00 ])
p = np.polyfit(X_high, Y_high, 2)
f_h = np.linspace(0, 6.1, 151)
y_h = p[0]*f_h**2 + p[1]*f_h + p[2]
pl.plot(f_h, y_h, "o", color ="orange", markersize = 3)


#righter

X_r = np.array([9.528242250e+00, 8.221729009e+00, 5.928072430e+00, 4.147343271e+00, 2.908575161e+00, 1.166557506e+00])
Y_r = np.array([3.043346616e+01, 2.754647629e+01, 2.230961094e+01, 1.730773314e+01, 1.385005922e+01, 7.941800880e+00])
p = np.polyfit(X_r, Y_r, 2)
f_r = np.linspace(1.13, 9.45, 151)
y_r = p[0]*f_r**2 + p[1]*f_r + p[2]
pl.plot(f_r, y_r, "o", color ="green", markersize = 3)



# righter_1

X_f_1 = np.array([1.265148042e+01, 9.071970065e+00, 6.415478107e+00, 2.292674435e+00])
Y_f_1 = np.array([3.034636628e+01, 2.421363630e+01, 1.884749758e+01, 8.761559032e+00 ])
p = np.polyfit(X_f_1, Y_f_1, 2)
f_f_1 = np.linspace(0.85, 14.36, 151)
y_f_1 = p[0]*f_f_1**2 + p[1]*f_f_1 + p[2]
pl.plot(f_f_1, y_f_1, "o", color ="red", markersize = 3)


# righter_2

X_f_2 = np.array([1.964667339e+01, 1.560665323e+01, 1.034909274e+01, 7.747983871e+00, 4.372076613e+00])
Y_f_2 = np.array([3.242507304e+01, 2.865945074e+01, 2.156606920e+01, 1.683714817e+01, 1.044434753e+01])
p = np.polyfit(X_f_2, Y_f_2, 2)
f_f_2 = np.linspace(1.66, 20.2, 151)
y_f_2 = p[0]*f_f_2**2 + p[1]*f_f_2 + p[2]
pl.plot(f_f_2, y_f_2, "o", color ="violet", markersize = 3)

# main diag
X_m = np.array([3.099928504e+01, 2.420046664e+01, 1.803200226e+01, 1.370957467e+01, 7.833774661e+00])
Y_m = np.array([3.291444696e+01, 2.540185274e+01, 1.911580451e+01, 1.447792747e+01, 8.115220118e+00])
p = np.polyfit(X_m, Y_m, 2)
f_m = np.linspace(4.3, 31.07, 151)
y_m = p[0]*f_m**2 + p[1]*f_m + p[2]
pl.plot(f_m, y_m, "o", color ="blue", markersize = 3)

#lower than main diag
X_low = np.array([6.558114919e+00, 1.452746976e+01, 2.183271169e+01, 2.714561492e+01, 3.237550403e+01])
Y_low = np.array([4.652240260e+00, 1.196035714e+01, 1.828811688e+01, 2.372464286e+01, 2.916116883e+01])
p = np.polyfit(X_low, Y_low, 2)
f_l = np.linspace(6.2, 32.87, 151)
y_l = p[0]*f_l**2 + p[1]*f_l + p[2]
pl.plot(f_l, y_l, "o", color ="brown", markersize =3)
pl.show()





