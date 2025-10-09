# simulation.py

import random
from environment import Environment
from data_collector import DataCollector

class Simulation:
    """Main simulation manager controlling the SEIRV process."""

    def __init__(self, population=1000, beta=0.10, sigma=0.20, gamma=0.14, nu=0.02,
                 mask_effect=0.60, vaccine_effect=0.85):
        self.environment = Environment(population)
        self.data_collector = DataCollector()
        self.day = 0

        # Parameters
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        self.nu = nu
        self.mask_effect = mask_effect
        self.vaccine_effect = vaccine_effect

        # Initialize one infected case
        self.environment.population[0].state = 'I'

    def infection_probability(self, agent_i, agent_j):
        """Equation 6: P(infection) = β * (1 - e_m) * (1 - e_v)"""
        e_m = self.mask_effect if agent_i.mask or agent_j.mask else 0
        e_v = self.vaccine_effect if agent_j.vaccinated else 0
        return self.beta * (1 - e_m) * (1 - e_v)

    def step(self):
        """Perform one day of simulation."""
        self.day += 1
        agents = self.environment.population

        # Infection spread by random contacts
        for agent in agents:
            if agent.state == 'I':
                contacts = random.sample(agents, k=min(10, len(agents)))
                for other in contacts:
                    if other.state == 'S':
                        p = self.infection_probability(agent, other)
                        if random.random() < p:
                            other.state = 'E'
        # Verification print statements
        for agent in agents:
            if agent.state == 'I':
                contacts = random.sample(agents, k=min(10, len(agents)))
                for other in contacts:
                    if other.state == 'S':
                        p = self.infection_probability(agent, other)
                        if random.random() < p:
                            other.state = 'E'
                            print(
                                f"Day {self.day}: Agent {agents.index(agent)} infected Agent {agents.index(other)} (p={p:.3f})")
        # Disease progression
        for agent in agents:
            if agent.state == 'E' and random.random() < self.sigma:
                agent.state = 'I'
            elif agent.state == 'I' and random.random() < self.gamma:
                agent.state = 'R'
            elif agent.state == 'S' and random.random() < self.nu:
                agent.state = 'V'

        # Record daily counts
        self.data_collector.record(self.day, agents)
