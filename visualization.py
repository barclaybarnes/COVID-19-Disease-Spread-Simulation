# visualization.py

import matplotlib.pyplot as plt
import pandas as pd

def plot_epidemic_curve(csv_file="simulation_results.csv"):
    """Plot infection dynamics over time."""
    df = pd.read_csv(csv_file)
    plt.figure(figsize=(8, 4))
    plt.plot(df["day"], df["S"], label="Susceptible")
    plt.plot(df["day"], df["E"], label="Exposed")
    plt.plot(df["day"], df["I"], label="Infected", linewidth=2)
    plt.plot(df["day"], df["R"], label="Recovered")
    plt.plot(df["day"], df["V"], label="Vaccinated")
    plt.xlabel("Day")
    plt.ylabel("Population")
    plt.legend()
    plt.title("COVID-19 Simulation (SEIRV)")
    plt.tight_layout()
    plt.show()

