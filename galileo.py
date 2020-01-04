from iminuit import Minuit
import sys
from regex import findall, match
from math import pow

h = []
d = []
with open(sys.argv[1]) as input:
    line = input.readlines()
    for i in range(0, len(line)):
        if match(r"^\s*!.*$",line[i]):
            continue
        elif match(r"^\s*(\d+)\s*(\d+)\s*$", line[i]):
            a = findall(r"^\s*(\d+)\s*(\d+)\s*$",line[i])
            h.append(float(a[0][0]))
            d.append(float(a[0][1]))

sigma = float(sys.argv[2])
def line(x, a, b):
    return a * x ** b

def func(a, b):
    s = 0
    for i in range(0, len(d)):
        the = line(h[i],a,b)
        s = s + ((d[i] - the) ** 2) / sigma
    return s

m = Minuit(func, a=50, b=0.5, error_a=1, error_b=0.1,errordef=1)
print(m.values)
m.migrad()
print(m.values)
m.hesse()

