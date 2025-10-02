# run_multiple.py

from simulation import Simulation
import config
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_multiple(n_runs=10, population=1000, timesteps=200):
    """Run multiple stochastic simulations to compute mean infection curve."""
    all_runs = []

    for r in range(n_runs):
        sim = Simulation(population=population,
                         beta=config.BETA, sigma=config.SIGMA,
                         gamma=config.GAMMA, nu=config.NU,
                         mask_effect=config.MASK_EFFECT,
                         vaccine_effect=config.VACC_EFFECT)
        for _ in range(timesteps):
            sim.step()
        df = pd.DataFrame(sim.data_collector.records)
        all_runs.append(df["I"].values)

    mean_I = np.mean(all_runs, axis=0)
    std_I = np.std(all_runs, axis=0)

    plt.figure(figsize=(8, 4))
    plt.plot(mean_I, label="Mean Infected")
    plt.fill_between(range(len(mean_I)),
                     mean_I - std_I, mean_I + std_I, alpha=0.3)
    plt.title("Mean Infection Curve Across 10 Simulations")
    plt.xlabel("Day")
    plt.ylabel("Infected Count")
    plt.legend()
    plt.tight_layout()
    plt.show()
