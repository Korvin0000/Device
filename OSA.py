import sys
import socket
import re
import time

class Error:
    def __init__ (self, message):
        self.message = message
    def __str__ (self):
        return self.message
    def __repr__ (self):
        return self.message

def get_data_from_socket(sck, timeout=0.2):
    data = ""
    sck.settimeout(None)
    data = sck.recv(1024)
    sck.settimeout(timeout)

    while 1:
        line = ""
        try:
            line = sck.recv(1024)
        except socket.timeout:
            break

        if line == "":
            break

        data += line

    return data

class OSA_AQ6370(socket.socket):
    "Optical Spectrum Analyzer ANDO AQ6370 basic methods"
    def __init__ (self, host, port, short_timeout=2, long_timeout=100, trace='TRA', center=1575, span=80):
        self.timeoutShort = short_timeout # seconds
        self.timeoutLong = long_timeout
        self.trace = trace
        self.center = center
        self.span = span

        # hardcoded buffer sizes
        self.dataBufferLength = 65536
        self.commandBufferLength = 1024

        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.settimeout(self.timeoutShort)
        self.send(b"OPEN \"anonymous\"\n\n")
        #get_data_from_socket(self, self.short_timeout)
        self.send(b":ABORt\n")
        # check whether we connect to an OSA
        self.send(b"*IDN?\n")
        get_data_from_socket(self, self.timeoutShort)

        self.send(("SENSe:Wavelength:CENter " + str(self.center) + "nm\n").encode())
        self.send(("SENSe:Wavelength:SPAN " + str(self.span) + "nm\n").encode())

        self.send(b':DISPlay:TRACe:Y1:SPACing LOGarithmic\n')
        #get_data_from_socket(self, self.timeoutShort)
    def SetTimeouts(self, timeout_short, timeout_long):
        self.timeoutShort = timeout_short
        self.timeoutLong = timeout_long
    def SetTrace(self, trace):
        self.trace = trace
    def UseShortTimeout(self):
        self.settimeout(self.timeoutShort)
    def UseLongTimeout(self):
        self.settimeout(self.timeoutLong)
    def PullSpectrum(self, center, span):
        self.center = center
        self.span = span
        self.send(b':INITiate:IMMediate\n')
        self.send((':TRACe:X? ' + self.trace + '\n').encode())
        x_str = get_data_from_socket(self, self.timeoutShort)
        self.send((':TRACe:Y? ' + self.trace + '\n').encode())
        y_str = get_data_from_socket(self, self.timeoutShort)
        return x_str, y_str
