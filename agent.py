class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.state = 'S'  # S, E, I, R, V
        self.mask = False
        self.vaccinated = False
        self.infection_timer = 0