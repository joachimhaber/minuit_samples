import apfel
import matplotlib.pyplot as plt
import sys
from regex import split


def x_extractor(fInput):
    with open(fInput) as input:
        line = input.readlines()
        a = split(r"\s", line[3])
    return a

x= []
for item in x_extractor(sys.argv[1]):
    try:
        if float(item) > 0.0001:
            x.append(float(item))
    except:
        continue
print(x)
apfel.SetQLimits(1.3, 100000)
apfel.SetProcessDIS("NC")
apfel.SetTargetDIS("neutron")
apfel.InitializeAPFEL_DIS()
apfel.ComputeStructureFunctionsAPFEL(1.3, 20)

f2N = []
for item in x:
    f2N.append(apfel.F2light(item))

apfel.SetQLimits(1.3, 100000)
apfel.SetProcessDIS("NC")
apfel.SetTargetDIS("proton")
apfel.InitializeAPFEL_DIS()
apfel.ComputeStructureFunctionsAPFEL(1.3, 20)

f2P = []
for item in x:
    f2P.append(apfel.F2light(item))

f2D = []
for i in range(0, len(f2P)):
    f2D.append((f2N[i] + f2P[i]) / 2)

with open('output.dat', 'w+') as fil:
    for i in range(0, len(f2D)):
        fil.writelines(str(x[i]) + ", " + str(f2N[i]) + ", " + str(f2P[i]) + ", " + str(f2D[i]) + "\n")










