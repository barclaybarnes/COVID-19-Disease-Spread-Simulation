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

