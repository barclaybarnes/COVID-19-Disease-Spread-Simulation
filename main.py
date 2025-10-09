# main.py
from simulation import Simulation
from visualization import plot_epidemic_curve
import config

if __name__ == "__main__":
    sim = Simulation(population=1000,
                     beta=config.BETA,
                     sigma=config.SIGMA,
                     gamma=config.GAMMA,
                     nu=config.NU,
                     mask_effect=config.MASK_EFFECT,
                     vaccine_effect=config.VACC_EFFECT)

    for _ in range(200):
        sim.step()

    agents = sim.environment.population
    total_recovered = sum(1 for agent in agents if agent.state == 'R')
    print(f"Total recovered: {total_recovered}")
    sim.data_collector.to_csv("simulation_results.csv")
    plot_epidemic_curve("simulation_results.csv")


