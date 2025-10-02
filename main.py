# main.py
from simulation import Simulation

if __name__ == "__main__":
    sim = Simulation(population=1000)
    for _ in range(10):
        sim.step()
    print("Simulation initialized successfully.")
