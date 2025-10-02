# main.py (update)
from simulation import Simulation
import config

if __name__ == "__main__":
    sim = Simulation(
        population=1000,
        beta=config.BETA,
        sigma=config.SIGMA,
        gamma=config.GAMMA,
        nu=config.NU
    )
    for _ in range(100):
        sim.step()
    print("Simulation complete.")

