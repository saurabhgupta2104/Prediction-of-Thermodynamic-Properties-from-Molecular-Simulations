import math
def simple_cube_coor(natoms, mm, density, boxlen):


    z = 1            #for scc

    N = 6.023*(10**23)
    a3 = (z*mm)/(N*density)
    a = math.pow(a3, (1.0/3.0))
    a *= 10**8 
    # l = math.pow((a3*natoms), (1.0/3.0))
    if boxlen%a == 0:
        n = int(boxlen/a)
    else:
        n = int(boxlen/a)+1
    # print("n , a ", n, a)

    coor = []
    f = 1
    for i in range(n):
        if f:
            for j in range(n):
                if f:
                    for k in range(n):
                        if len(coor) == natoms:
                            f = 0
                            break
                        coor.append([k*a, j*a, i*a])
        else:
            break
    return coor
