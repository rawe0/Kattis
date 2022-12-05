 
from math import gcd
import sys


def find_steps (a, b, n):
 
    i = 0
    while i * a <= n:
        if (n - (i * a)) % b == 0:
           return i + int((n - (i * a)) / b)
        i = i + 1
     
    return -1

def isPossible(a, b, c):
    return (c % gcd(a, b) == 0)


for arg in sys.stdin:
    
    parameters = arg.split()
    
    f = int(parameters[0])
    s = int(parameters[1])
    g = int(parameters[2])
    u = int(parameters[3])
    d = int(parameters[4])

    g = g-s
    d = -d

    if (isPossible(d, u, g)):
        print(find_steps(d, u, g))
    else:
        print("use the stairs")

 

 