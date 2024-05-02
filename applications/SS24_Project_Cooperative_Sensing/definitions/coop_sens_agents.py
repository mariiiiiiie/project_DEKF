import numpy as np
import math

from scioi_py_core import core
from applications.SS24_Project_Cooperative_Sensing.definitions.coop_sens_dynamics import Robot_Dynamics
from scioi_py_core.core.physics import PhysicalBody


class CoopSensPhysics(PhysicalBody):

    def update(self, *args, **kwargs):
        pass

    def _calcProximitySphere(self):
        pass

    def _getProximitySphereRadius(self):
        pass


class CoopSensAgent(core.agents.DynamicAgent):
    object_type = 'CoopSensAgent'
    dynamics_class = Robot_Dynamics
    space = core.spaces.Space2D()

    y: int

    def __init__(self, name: str, world, agent_id, x :float, y: float, psi : float, radius: float, fov: float, *args, **kwargs):
        self.dynamics = self.dynamics_class()
        super().__init__(name=name, world=world, agent_id=agent_id, *args, **kwargs)


        self.state['pos']['x'] = x
        self.state['pos']['y'] = y
        self.state['psi'] = psi
        self.radius = radius
        self.fov = fov
        self.physics = CoopSensPhysics()

        core.scheduling.Action(name='measuring', function=self.measuring, object=self)
        core.scheduling.Action(name='prediction', function=self.prediction, object=self)

    # ------------------------------------------------------------------------------------------------------------------

    def prediction(self):
        print(f"Step: {self.scheduling.tick_global} Agent {self.agent_id} - Prediction Phase")
        # Here comes the code for prediction we want to make the prediction step
        # self.prediction = self.getPrediction()

    def measuring(self):
        # here comes all the stuff happening in the measuring phase for each agent
        print(f"Step: {self.scheduling.tick_global} Agent {self.agent_id} - Measuring Phase")

        agents_in_fov = self.getAgentsinFov()
        for agent in agents_in_fov:
            print(f"Step: {self.scheduling.tick_global} Agent {self.agent_id} - measures Agent {agent.agent_id} - Measuring Phase")



    def getAgentsinFov(self):
        agents_in_fov = []

        # calcul of vectors
        v_ori = np.array([math.cos(self.state['psi'].value), math.sin(self.state['psi'].value)])
        alpha = self.fov / 2
        rotmat1 = np.array([[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)]])
        rotmat2 = np.array([[math.cos(-alpha), -math.sin(-alpha)], [math.sin(-alpha), math.cos(-alpha)]])
        v1 = rotmat1 @ v_ori
        v2 = rotmat2 @ v_ori


        #for agent_j in self.world.agents:
        for agent_id, agent_j in (self.world.agents.items()):
            # not agent itself
            if agent_j is self:
                continue

            # Calcul the relative position of agent_j  according to self.agent
            state_rel = {'x': agent_j.state['pos']['x'] - self.state['pos']['x'], 'y': agent_j.state['pos']['y'] - self.state['pos']['y']}
            vec_rel = np.array([state_rel['x'], state_rel['y']])
            dist = np.linalg.norm(vec_rel)

            # Check if agent agent_j is in the FOV of self.agent
            if np.cross(v1, vec_rel) * np.cross(v1, v2) >= 0 and np.cross(v2, vec_rel) * np.cross(v2,
                                                                                                  v1) >= 0 and dist <= self.radius:
                agents_in_fov.append(agent_j)

        return agents_in_fov

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    def _getParameters(self):
        ...

    def _getSample(self):
        ...

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value: (list, np.ndarray, core.spaces.State)):
        self._input = self.dynamics.input_space.map(value)
