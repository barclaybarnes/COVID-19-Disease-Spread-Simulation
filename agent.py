# agent.py

class Agent:
    def __init__(self, agent_id, mask=False, vaccinated=False):
        self.id = agent_id
        self.state = 'S'  # S, E, I, R, or V
        self.mask = mask
        self.vaccinated = vaccinated
        self.infection_timer = 0
        self.ever_infected = False
