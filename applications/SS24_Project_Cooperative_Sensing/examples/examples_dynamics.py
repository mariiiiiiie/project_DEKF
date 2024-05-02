from applications.SS24_Project_Cooperative_Sensing.definitions.coop_sens_dynamics import Robot_Dynamics
import math


def example_dynamics_1():
    dyn = Robot_Dynamics()

    dyn.input = [-1, -1]

    for i in range(0, 10):
        dyn.update()
        print(dyn.state['psi'])
        #typetest = type(dyn.state['psi'])
        #psi_value = dyn.state['psi'].value # ou dyn.state['psi'].value
        #b = math.sin(psi_value)
        #print (b, typetest)


if __name__ == '__main__':
    example_dynamics_1()
