# environment.py
class Environment:
    def __init__(self, population_size):
        from agent import Agent
        self.population = [Agent(i) for i in range(population_size)]
