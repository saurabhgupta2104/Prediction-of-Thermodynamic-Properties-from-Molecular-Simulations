import copy
import math



def pbc(d, boxlen):
    # print(d, boxlen)

    if d > boxlen/2:
        d = d - boxlen
    if d < -1*(boxlen/2):
        d = d + boxlen

    if -1*(boxlen/2)< d < boxlen/2:
        return d
    else:
        d = pbc(d, boxlen)

    return d

def disp(a, b, boxlen):
    d = a-b
    if d > boxlen/2:
        d = d - boxlen
    if d < -1*(boxlen/2):
        d = d + boxlen

    return d


def force_calculation(c, rc, boxlen, mm, proton_mass, epsilon, sigma):
    ac = []
    for p in range(len(c)):
        fx = 0
        fy = 0
        fz = 0

        for q in range(len(c)):
            if p != q:

                dx = disp(c[p][0], c[q][0], boxlen)
                dy = disp(c[p][1], c[q][1], boxlen)
                dz = disp(c[p][2], c[q][2], boxlen)

                dr = math.sqrt(dx*dx+dy*dy+dz*dz)
                # print("dr, dx, dy, dz ",dr, dx, dy, dz)
                if 3 < dr < rc:

                    a = (sigma / dr)

                    f = 2*pow(a, 12)- pow(a, 6)
                    f= f*24*epsilon/dr
                    fx += f*(dx/dr)
                    fy += f*(dy/dr)
                    fz += f*(dz/dr)

        ac.append([fx/(mm * proton_mass), fy/(mm * proton_mass), fz/(mm * proton_mass)])
    # print(ac)
    return ac


def verlet_calculation(coor, sigma, epsilon, boxlen, dt, rc, mm, nsteps, nsave, lsteps, proton_mass, natoms, nstore):

    saver= open("Save_Coor.txt","w+")
    t = 0.0
    acc = []
    acc = force_calculation(coor, rc, boxlen, mm, proton_mass, epsilon, sigma )

    coor2 = []

    for i in range(lsteps, nsteps):

        if i == 0:
            for j in range(natoms):

                x = coor[j][0] + (dt**2)*acc[j][0]*10**(4)
                x = pbc(x, boxlen)

                y = coor[j][1] + (dt**2)*acc[j][1]*10**(4)
                y = pbc(y, boxlen)

                z = coor[j][2] + (dt**2)*acc[j][2]*10**(4)
                z = pbc(z, boxlen)

                coor2.append([x, y, z])


        else:

            acc = force_calculation(coor2, rc, boxlen, mm, proton_mass, epsilon, sigma)
            # print(acc)
            for j in range(natoms):

                x = 2*coor2[j][0] - coor[j][0]  + (dt**2)*acc[j][0]*10**(4)
                x = pbc(x, boxlen)

                y = 2*coor2[j][1] - coor[j][1] + (dt**2)*acc[j][1]*10**(4)
                y = pbc(y, boxlen)

                z = 2*coor2[j][2] - coor[j][2] + (dt**2)*acc[j][2]*10**(4)
                z = pbc(z, boxlen)

                coor[j] = coor2[j]
                coor2[j] = [x, y, z]

            if i % nsave == 0:

                saver.write("t = {} \n".format(t))
                saver.write("{} \n".format(i))
                t = t+1

                for stof in range(len(coor2)):  #stof :- save to file

                    saver.write("AR     {}     {}  {} {} \n".format(i, round(coor2[stof][0], 3), round(coor2[stof][1], 3), round(coor2[stof][2], 3)))

            if i % nstore == 0:
                storer = open("Store_coor.txt","w+")
                storer.write("lstep = {} \n".format(i))


                for stof in range(len(coor2)):  #stof :- save to file

                    storer.write("AR     {}     {}  {} {} \n".format(i,  round(coor2[stof][0], 3), round(coor2[stof][1], 3), round(coor2[stof][2], 3)))


                storer.close()
    saver.close()
    import os
    os.remove("Store_coor.txt")


                # print(acc)

                # print("Values of iteration ", i)
                # for b in range(len(coor2)):
                #     # print(coor[b])
                #     print(coor2[b])
