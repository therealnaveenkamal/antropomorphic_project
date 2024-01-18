#!/usr/bin/env python3

import math

class IK():

    def __init__(self, DH_parameters):
        self.DH_parameters_ = DH_parameters

    def compute_ik(self, Pee_x, Pee_y, Pee_z, theta_2_config = "plus", theta_3_config = "plus"):

        possible_solution = False
        r2 = 0.0
        r3 = 0.0

        if("r2" in self.DH_parameters_):
            r2 = self.DH_parameters_["r2"]
        if("r3" in self.DH_parameters_):
            r3 = self.DH_parameters_["r3"]
        
        print("Input Data===== theta_2_config = "+str(theta_2_config))
        print("Input Data===== theta_2_config = "+str(theta_3_config))        
        print("Pee_x = "+str(Pee_x))
        print("Pee_y = "+str(Pee_y))
        print("Pee_z = "+str(Pee_z))
        print("r2 = "+str(r2))
        print("r3 = "+str(r3))

        theta_1_1 = math.atan2(Pee_y, Pee_x)
        theta_1_2 = math.atan2(math.sin(theta_1_1 + math.pi), math.cos(theta_1_1 + math.pi))

        theta_1 = theta_1_1
        if(theta_2_config == "plus"):
            theta_1 = theta_1_1
        else:
            theta_1 = theta_1_2

        x = Pee_x * math.cos(theta_1) + Pee_y * math.sin(theta_1)
        y = Pee_z
        theta_3_1 = math.acos((x**2 + y**2 - r2**2 - r3**2)/(2 * r2 * r3))
        theta_3_2 = math.atan2(math.sin(-theta_3_1), math.cos(-theta_3_1))

        theta_3 = theta_3_1
        if(theta_3_config == "plus"):
            theta_3 = theta_3_1
        else:
            theta_3 = theta_3_2

        tng1 = math.atan2(y, x)
        tng2 = math.atan2(r3*math.sin(theta_3), r2 + r3 * math.cos(theta_3))
        theta_2 = math.atan2(math.sin(tng1-tng2), math.cos(tng1-tng2))

        if (-math.pi/4 <= theta_2 <= 3*math.pi/4 and -3*math.pi/4 <= theta_3 <= 3*math.pi/4):
            possible_solution = True

        return [theta_1, theta_2, theta_3], possible_solution



def calculate_ik(Pee_x, Pee_y, Pee_z, DH_parameters, theta_2_config, theta_3_config):

    ik = IK(DH_parameters = DH_parameters)
    thetas, possible_solution = ik.compute_ik(Pee_x=Pee_x, Pee_y=Pee_y, Pee_z=Pee_z, theta_2_config=theta_2_config, theta_3_config=theta_3_config)

    print("Angles thetas solved ="+str(thetas))
    print("possible_solution = "+str(possible_solution))
    print("\n")

    return thetas, possible_solution

if __name__ == '__main__':
    
    r2 = 1.0
    r3 = 1.0
    DH_parameters={"r2":r2, "r3":r3}
    Pee_x = 0.5
    Pee_y = 0.6
    Pee_z = 0.7
    calculate_ik(Pee_x=Pee_x, Pee_y=Pee_y, Pee_z=Pee_z, DH_parameters=DH_parameters, theta_2_config = "plus", theta_3_config = "plus")
    calculate_ik(Pee_x=Pee_x, Pee_y=Pee_y, Pee_z=Pee_z, DH_parameters=DH_parameters, theta_2_config = "plus", theta_3_config = "minus")
    calculate_ik(Pee_x=Pee_x, Pee_y=Pee_y, Pee_z=Pee_z, DH_parameters=DH_parameters, theta_2_config = "minus", theta_3_config = "plus")
    calculate_ik(Pee_x=Pee_x, Pee_y=Pee_y, Pee_z=Pee_z, DH_parameters=DH_parameters, theta_2_config = "minus", theta_3_config = "minus")