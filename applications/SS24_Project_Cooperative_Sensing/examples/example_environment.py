import math

from applications.SS24_Project_Cooperative_Sensing.definitions.coop_sens_agents import CoopSensAgent
from applications.SS24_Project_Cooperative_Sensing.definitions.coop_sens_environment import \
    EnvironmentBase_CooperativeSensing


class CoopSens_Example_Environment_1(EnvironmentBase_CooperativeSensing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agent1 = CoopSensAgent(name='Agent 1', world=self.world, agent_id=1, x = 1.0, y = 2.0, psi = 0.0, radius = 2, fov = 90.0)
        self.agent2 = CoopSensAgent(name='Agent 2', world=self.world, agent_id=2, x = 2.0, y = 2.5, psi = 0.0, radius = 2, fov = 90.0)
        self.agent3 = CoopSensAgent(name='Agent 3', world=self.world, agent_id=3, x = 2.5, y = 2.0, psi = math.pi/2, radius = 2, fov = 90.0)


def example_1():
    env = CoopSens_Example_Environment_1()
    env.init()
    env.start(steps=2)


if __name__ == '__main__':
    example_1()