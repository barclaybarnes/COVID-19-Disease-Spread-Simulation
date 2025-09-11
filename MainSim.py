import random
from enum import Enum
import matplotlib.pyplot as plt


class HealthState(Enum):
    SUSCEPTIBLE = 1
    EXPOSED = 2
    INFECTED = 3
    RECOVERED = 4
    VACCINATED = 5


class Person:
    def __init__(self, pid, vaccinated=False, mask=False):
        self.id = pid
        self.state = HealthState.SUSCEPTIBLE
        self.mask = mask
        self.vaccinated = vaccinated
        self.days_infected = 0

    def interact(self, other, transmission_prob=0.1):
        """Simulate interaction with another person."""
        if self.state == HealthState.INFECTED and other.state == HealthState.SUSCEPTIBLE:
            if random.random() < transmission_prob:
                other.state = HealthState.EXPOSED

        elif other.state == HealthState.INFECTED and self.state == HealthState.SUSCEPTIBLE:
            if random.random() < transmission_prob:
                self.state = HealthState.EXPOSED

    def update_state(self, incubation_period=3, infection_duration=7):
        """Update health state based on current state and counters."""
        if self.state == HealthState.EXPOSED:
            self.days_infected += 1
            if self.days_infected >= incubation_period:
                self.state = HealthState.INFECTED
                self.days_infected = 0

        elif self.state == HealthState.INFECTED:
            self.days_infected += 1
            if self.days_infected >= infection_duration:
                self.state = HealthState.RECOVERED
                self.days_infected = 0