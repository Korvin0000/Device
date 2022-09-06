import os
import numpy as np
from time import sleep, time
from datetime import datetime
import glob

import matplotlib.pyplot as plt
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.widgets import Button, Cursor, SpanSelector, RadioButtons
from OSA import OSA_AQ6370, get_data_from_socket


path = 'C:\\Users\\Guest\\Desktop\\laser_on_chip\\'
Stuff = glob.glob( path + '*.txt')
for j in Stuff:
    #For Map r(p, la)
    r_, f_ = np.genfromtxt( j, dtype = float, unpack = True, usecols = [ 1, 0 ], delimiter = ';' )
    
class SpectrumPlot(object):
    
    def __init__(self, **kwargs):
        plt.ion()
        
    def update(self, wavelength, power, label=time()):
        plt.plot(wavelength, power);
        plt.xlabel('Wavelength, nm')
        plt.ylabel('Reflectivity, dBm')
        plt.xlim(1520, 1580)
        plt.ylim(-80, 10)
        plt.grid()
        plt.pause(0.001);
        plt.cla();
    
def fileAppend(filename, data_string):
    f = open(filename, 'a')
    f.write(data_string + '\n')
    f.close()
        

def decodeOSADataToNpArray(data_bytes):
    data_str = data_bytes.decode(errors='ignore')
    data = np.array(data_str.strip().split(',')).astype(float)
    return data


def send_measure(r, p, f, s, client): #setting the current 
    if r > 3300 or p > 700 or f > 3300: #threshold for currents
        print("Incorrect Input Values")
        return
    
    print(f'>>> set: r={r} p={p} f={f} s={s}')    
    rw = client.write_register(5, r, unit=0x1) #LT_RBDR; 33
    pw = client.write_register(6, p, unit=0x1) #LT_PM; 34
    fw = client.write_register(7, f, unit=0x1) #LT_FBDR; 35
    sw = client.write_register(36, s, unit=0x1) #LT_SOA; 36
    sleep(0.001)

def get_currents(client): #reading the set current
    rq = client.read_holding_registers(5, 1, unit=0x1) #LT_RBDR
    r = rq.registers[0]
    rq = client.read_holding_registers(6, 1, unit=0x1) #LT_PM
    p = rq.registers[0]
    rq = client.read_holding_registers(7, 1, unit=0x1) #LT_FBDR
    f = rq.registers[0]
    rq = client.read_holding_registers(36, 1, unit=0x1) #LT_SOA
    s = rq.registers[0]
    print(f'<<  get: r={r} p={p} f={f} s={s}')

    return [r,p,f,s]    

def take_characteristic(client_): #experiment
       
    global r_
    global f_
    s = 3000
    
    for i in range(len(r_)):    
        r = int(r_[i])
        f = int(f_[i])
        
        for k in range(0, 710, 24):
            
            p = k
            
            set_c = [round(r), round(p), round(f), s]
            send_measure(set_c[0], set_c[1], set_c[2], set_c[3], client_)
            real_c = get_currents(client)
            snap(set_c, real_c) 
            

sp = SpectrumPlot()

def snap(set_c, real_c):
    
    # spectrum scan
    x_bytes, y_bytes = osa.PullSpectrum(specCenter, specSpan) 
    current_time = datetime.strftime(datetime.now(), '%H-%M-%S')

    x = decodeOSADataToNpArray(x_bytes) * 1e9  # to nm
    y = decodeOSADataToNpArray(y_bytes)

    # data writing
    current_time = datetime.strftime(datetime.now(), '%Y.%m.%d %H-%M-%S')
    specFilename = path + current_time + '.txt'
    print("Save to file:", specFilename)
    specData = np.array([x, y]).T

    temp = client.read_input_registers(2, 1, unit=1)
    temp = temp.registers[0]/100
    print("Temp:", temp)
    head = f'set\nr:{set_c[0]}\np:{set_c[1]}\nf:{set_c[2]}\ns:{set_c[3]}\nget\nr:{real_c[0]}\np:{real_c[1]}\nf:{real_c[2]}\ns:{real_c[3]}\ntemp:{temp}'

    try:
        np.savetxt(specFilename, specData, fmt="%.8e", delimiter=';', header=head)
    except Exception as e:
        pass
  
    sp.update( x, y ) #draw spectrum from OSA

# OSA INIT
osaHOST = '192.168.0.74'
osaPORT = 10001
osaTraceW = 'TRB'
osaTraceR = 'TRC'

osa = OSA_AQ6370(host=osaHOST, port=osaPORT, trace=osaTraceW)

# TRACE
osa.send((':TRACe:ATTRibute:' + osaTraceW + ' WRITe\n').encode())
osa.send((':TRACe:STATe:' + osaTraceR + ' ON\n').encode())

# SETUP parameters on OSA
specCenter = 1550
specSpan = 60
specResolution = 0.02
specSenceMode = 'NORMAL'
specAverageCount = 1

osa.send((':SENSe:Wavelength:CENter ' + str(specCenter) + 'nm\n').encode())
osa.send((':SENSe:Wavelength:SPAN ' + str(specSpan) + 'nm\n').encode())
osa.send((':SENSe:BANDwidth:RESolution ' + str(specResolution) + 'nm\n').encode())
osa.send((':SENSe:SENSe ' + specSenceMode + '\n').encode())
osa.send((':SENSe:AVERage:COUNt ' + str(specAverageCount) + '\n').encode())
osa.send(':SENSe:SWEep:POINts:AUTO ON\n'.encode())


current_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M')
path = './data/' + current_time + '/' #saving files here
os.mkdir(path)


osa.send((':TRACe:ACTive ' + 'TRA' + '\n').encode())
osa.send((':TRACe:ACTive ' + osaTraceW + '\n').encode())

client = ModbusClient(method='rtu', port='COM3', timeout=1, baudrate=57600)

if client.connect() == True:
    
    take_characteristic(client) # getting a characteristic
    client.close()
    print('===== finish =====')
    
else:
    
    print("No")
