python
from simulation import Simulation
import config
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.widgets import CheckButtons

def seirv_ode(y, t, beta, sigma, gamma, nu):
    S, E, I, R, V = y
    N = S + E + I + R + V
    dSdt = -beta * S * I / N - nu * S
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    dVdt = nu * S
    return [dSdt, dEdt, dIdt, dRdt, dVdt]

def run_multiple(n_runs=50, population=5000, timesteps=200):
    # Collect per-run time series for each compartment
    runs_S = []
    runs_E = []
    runs_I = []
    runs_R = []
    runs_V = []

    for r in range(n_runs):
        sim = Simulation(population=population,
                         beta=config.BETA, sigma=config.SIGMA,
                         gamma=config.GAMMA, nu=config.NU,
                         mask_effect=config.MASK_EFFECT,
                         vaccine_effect=config.VACC_EFFECT)
        for _ in range(timesteps):
            sim.step()
        df = pd.DataFrame(sim.data_collector.records)

        # ensure columns exist and have expected length
        runs_S.append(df["S"].values[:timesteps])
        runs_E.append(df["E"].values[:timesteps])
        runs_I.append(df["I"].values[:timesteps])
        runs_R.append(df["R"].values[:timesteps])
        runs_V.append(df["V"].values[:timesteps])

    # compute means (and std if needed)
    mean_S = np.mean(np.vstack(runs_S), axis=0)
    mean_E = np.mean(np.vstack(runs_E), axis=0)
    mean_I = np.mean(np.vstack(runs_I), axis=0)
    mean_R = np.mean(np.vstack(runs_R), axis=0)
    mean_V = np.mean(np.vstack(runs_V), axis=0)

    # save averaged results to CSV (same per-day columns as simulation_results.csv)
    t = np.arange(timesteps)
    df_mean = pd.DataFrame({
        "Day": t,
        "S": mean_S,
        "E": mean_E,
        "I": mean_I,
        "R": mean_R,
        "V": mean_V
    })
    df_mean.to_csv("simulation_results_mean.csv", index=False)

    # ODE solution
    S0 = population - 1
    E0 = 0
    I0 = 1
    R0 = 0
    V0 = 0
    y0 = [S0, E0, I0, R0, V0]
    sol = odeint(seirv_ode, y0, t, args=(config.BETA, config.SIGMA, config.GAMMA, config.NU))
    ode_I = sol[:, 2]

    fig, ax = plt.subplots(figsize=(8, 4))
    abm_line, = ax.plot(mean_I, label="ABM Mean Infected")
    abm_fill = ax.fill_between(range(len(mean_I)),
                              mean_I - np.std(np.vstack(runs_I), axis=0),
                              mean_I + np.std(np.vstack(runs_I), axis=0),
                              alpha=0.3, label="ABM ±1 Std Dev")
    ode_line, = ax.plot(t, ode_I, 'r--', label="ODE Infected", visible=False)
    ax.set_title(f"ABM vs ODE: Mean Infection Curve Across {n_runs} Simulations")
    ax.set_xlabel("Day")
    ax.set_ylabel("Infected Count")
    ax.legend()

    # Checkbox widget
    rax = plt.axes([0.75, 0.5, 0.15, 0.1])
    check = CheckButtons(rax, ["Show ODE Infected"], [False])

    def func(label):
        ode_line.set_visible(not ode_line.get_visible())
        ax.legend()
        plt.draw()

    check.on_clicked(func)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_multiple()




