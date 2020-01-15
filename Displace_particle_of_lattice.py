import os
import random
import copy

def dir(a, lis, boxlen):
    b = random.randint(0,1)


    if b == 1:
        # lis[a] = lis[a] + (10**(-8))
        lis[a] = lis[a] + 1   #move 1 angstorm in positive direction
        if lis[a] > boxlen/2:
            lis[a] = lis[a] - boxlen


    if b == 0:
        # lis[a] = lis[a] - (10**(-8))
        lis[a] = lis[a] - 1      #move 1 angstorm in negative direction
        if lis[a] < -1*(boxlen/2):
            lis[a] = lis[a] + boxlen

    return lis


def Displace_particle(coor, neqilibrium, boxlen):

    for i in range(neqilibrium):
        # count = 0
        for j in range(len(coor)):
            a = random.randint(0,2)
            coor[j] = dir(a, coor[j], boxlen)

    return coor
