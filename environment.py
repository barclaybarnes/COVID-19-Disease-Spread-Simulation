# environment.py

from agent import Agent
import random

class Environment:
    """Holds population and manages random agent creation."""
    def __init__(self, population_size, mask_rate=0.6, vaccine_rate=0.4):
        self.population = []
        for i in range(population_size):
            mask = random.random() < mask_rate
            vaccinated = random.random() < vaccine_rate
            self.population.append(Agent(i, mask, vaccinated))

