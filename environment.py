# environment.py
# environment.py
import random

class Environment:
    """Holds population and manages random agent creation."""
    def __init__(self, population_size, mask_rate=0.6, vaccine_rate=0.4):
        from agent import Agent  # moved here to avoid circular import issue
        self.population = []
        for i in range(population_size):
            mask = random.random() < mask_rate
            vaccinated = random.random() < vaccine_rate
            self.population.append(Agent(i, mask, vaccinated))




