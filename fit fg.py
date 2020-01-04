import csv
import sys
import apfel
import numpy as np
from iminuit import Minuit
from math import sqrt, pow

def line(x, ag):
    return ag * pow(x,-0.1) * pow(1-x,5)



dataFile = open(sys.argv[1],"r")
reader = csv.reader(dataFile,delimiter=",")
data_y = []
data_x = []
apfel.InitializeAPFEL()
apfel.SetPerturbativeOrder(1)
Q0 = sqrt(2)
for row in reader:
        try:
            apfel.EvolveAPFEL(Q0, sqrt(float(row[1])))
            data_y.append(apfel.xPDF(0, float(row[0])))
            data_x.append(float(row[0]))
        except:
            continue
dataFile.close()

def func(ag):
    s = 0
    for i in range(0, len(data_x)):
        s = s + (data_y[i] - line(data_x[i], ag))
    return s

m = Minuit(func, ag=1.5, error_ag=0.0001, limit_ag=(1,10), errordef=1)
m.migrad()
print(m.values)
m.hesse()
print(m.errors)



