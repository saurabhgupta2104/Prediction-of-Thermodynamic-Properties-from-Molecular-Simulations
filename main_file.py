import importlib
from simple_cube_coor import  *
from Displace_particle_of_lattice import *
from Verlet_equation import*





boxlen =  18
mm = 39.95
tset = 100
temp = 100
natoms = 108
sigma = 3.4
epsilon = 1
dt = 5*(10**(-15))
msteps = 10000
nscale = 1
rc = 8
nsave = 500
nstore = 100
nsteps = 10000
lsteps = 0                              #last step where program terminated so update it accoringly
neqilibrium = 5000
nscale = 1
density = 1.39
proton_mass = 1.673 * 10**(-27)


import os.path
from os import path

coor = []

if os.path.exists("Store_coor.txt"):
    with open("Store_coor.txt") as handel:
        for h in handel:
            temp = list(h.strip().split())
            if temp[0] == "lstep":
                lstep = temp[2]
                print("code is starting from ",lstep)
            else:
                coor.append([float(temp[-3]), float(temp[-2]), float(temp[-1])])

    verlet_calculation(coor, sigma, epsilon, boxlen, dt, rc, mm,  nsteps, nsave, lsteps, proton_mass, natoms, nstore)


else:
    coor = simple_cube_coor(natoms, mm, density, boxlen)
    coor = Displace_particle(coor, neqilibrium, boxlen)
    verlet_calculation(coor, sigma, epsilon, boxlen, dt, rc, mm,  nsteps, nsave, lsteps, proton_mass, natoms, nstore)


