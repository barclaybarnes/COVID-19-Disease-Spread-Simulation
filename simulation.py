# simulation.py - Defines the Simulation class to manage the epidemic simulation.
import random

class Simulation:
    def __init__(self, population=1000, beta=0.1, sigma=0.2, gamma=0.14, nu=0.02):
        from environment import Environment
        self.environment = Environment(population)
        self.day = 0
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        self.nu = nu

    def step(self):
        self.day += 1
        for agent in self.environment.population:
            if agent.state == 'E' and random.random() < self.sigma:
                agent.state = 'I'
            elif agent.state == 'I' and random.random() < self.gamma:
                agent.state = 'R'
            elif agent.state == 'S' and random.random() < self.nu:
                agent.state = 'V'
    def infection_probability(self, agent_i, agent_j):
        """Eq. 6: P(infection) = beta * (1 - e_m) * (1 - e_v)"""
        e_m = 0.6 if agent_i.mask or agent_j.mask else 0
        e_v = 0.85 if agent_i.vaccinated else 0
        return self.beta * (1 - e_m) * (1 - e_v)

    def step(self):
        self.day += 1
        agents = self.environment.population
        for agent in agents:
            if agent.state == 'I':
                contacts = random.sample(agents, k=min(10, len(agents)))
                for other in contacts:
                    if other.state == 'S':
                        p = self.infection_probability(agent, other)
                        if random.random() < p:
                            other.state = 'E'
        # Update progression
        for agent in agents:
            if agent.state == 'E' and random.random() < self.sigma:
                agent.state = 'I'
            elif agent.state == 'I' and random.random() < self.gamma:
                agent.state = 'R'
            elif agent.state == 'S' and random.random() < self.nu:
                agent.state = 'V'