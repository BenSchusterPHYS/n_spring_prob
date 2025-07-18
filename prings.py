import matplotlib.pyplot as plt
import numpy as np

# Spring parameters:
num_springs = 1

# TODO: Make all for loops one big loop for easier input

# num_springs =  input("Number of springs to consider?")

# Get Spring Constants:
spring_const = [1]

#Left unimplemented for bug fixing sanity
#for i in range(num_springs):
#    kn = input(r"Spring constant of spring {i}:")
#    spring_const.append(float(kn))

anchor_pts = [[0,0]]
#for i in range(num_springs):
#    xn = input(r"x position of spring {i}:")
#    yn = input(r"y position of spring {i}")
#    anchor_pts.append([float(xn),float(yn)])


natural_len = [1]
#for i in range(num_springs):
#    Ln = input(r"Natural length of spring {i}:")
#    natural_len.append(float(Ln))

# Bundle parameters into standard list
spring_params = []
for i in range(num_springs):
    temp = []
    temp.append(anchor_pts[i])
    temp.append(spring_const[i])
    temp.append(natural_len[i])
    spring_params.append(temp)

print(spring_params)

# Mass parameters:
m = 1

# m = input(r"Input mass of spring:")

rx0 = 2
ry0 = 0

vx0 = 0
vy0 = 0

# rx0 = input(r"Input initial x position of spring")
# rx0 = input(r"Input initial y position of spring")
# vx0 = input(r"Input initial x velocity of spring")
# vy0 = input(r"Input initial x velocity of spring")

# Bundle parameters into standard list
mass_params = [[float(rx0),float(ry0)],[float(vx0),float(vy0)],m]
mass_params[0]

# Simulation parameters:
t0 = 0
tf = 10
dt = 1

def force(spring_num):
    # Get spring stretch from equilibrium 
    x_stretch = spring_params[spring_num][0][0] - mass_params[0][0]
    y_stretch = spring_params[spring_num][0][1] - mass_params[0][1]
    stretch = np.sqrt(x_stretch**2+y_stretch**2) - spring_params[spring_num][2]

    # Get direction of force
    x_dist = mass_params[0][0] - spring_params[spring_num][0][0]
    y_dist = mass_params[0][1] - spring_params[spring_num][0][1] 
    l = np.sqrt(x_dist**2 + y_dist**2)
    unit_vec = [x_dist / l,y_dist / l]
    force_x = -spring_params[spring_num][1] * stretch * unit_vec[0]
    force_y = -spring_params[spring_num][1] * stretch * unit_vec[1]
    return [force_x,force_y]

def euler():
    t = t0
    m_pos_x = [mass_params[0][0]]
    m_pos_y = [mass_params[0][1]]

    while t < tf:
        print("Spring:", spring_params)
        print("Mass:",mass_params)

        net_force = [0,0]

        for spring_num in range(0,num_springs):
            temp_force = force(spring_num)
            net_x = net_force[0] + temp_force[0]
            net_y = net_force[1] + temp_force[1]
            net_force = [net_x,net_y]
        print("Net Force: ",net_force)
        vnx = net_force[0] * dt / m + mass_params[1][0]
        vny = net_force[1] * dt / m + mass_params[1][1]

        mass_params[1][0] = vnx
        mass_params[1][1] = vny

        rnx = vnx * dt + mass_params[0][0]
        rny = vny * dt + mass_params[0][1]
        mass_params[0][0] = rnx
        mass_params[0][1] = rny 
        
        m_pos_x.append(rnx)
        m_pos_y.append(rny)
        
        t += dt
        
        for i in range(num_springs):
                plt.plot(spring_params[i][0][0],spring_params[i][0][1], 'o')
            
        print("--------------------------")
    plt.plot(m_pos_x, m_pos_y,'o')
    plt.show()

euler()