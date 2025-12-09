# validation.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import datetime
import os
import pandas as pd

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def seirv_ode(y, t, beta, sigma, gamma, nu):
    # y = [S, E, I, R, V]
    S, E, I, R, V = y
    N = S + E + I + R + V
    if N <= 0:
        # avoid division by zero
        return [0, 0, 0, 0, 0]
    dSdt = -beta * S * I / N - nu * S
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    dVdt = nu * S
    return [dSdt, dEdt, dIdt, dRdt, dVdt]

def run_validation(beta=0.10, sigma=0.20, gamma=0.14, nu=0.02,
                   N=1000, E0=1, I0=1, R0=0, V0=0, days=200,
                   overlay_abm=True, abm_csv="simulation_results.csv"):
    log("Starting SEIRV ODE validation...")

    # initial conditions
    S0 = float(N - E0 - I0 - R0 - V0)
    y0 = [S0, float(E0), float(I0), float(R0), float(V0)]
    t = np.linspace(0, days, days+1)

    log(f"Parameters: beta={beta}, sigma={sigma}, gamma={gamma}, nu={nu}, N={N}")
    log(f"Initial conditions (S,E,I,R,V): {y0}")

    # solve ODE
    sol = odeint(seirv_ode, y0, t, args=(beta, sigma, gamma, nu))
    S, E, I, R, V = sol.T

    # diagnostics
    log(f"ODE Solution ranges - S: [{S.min():.2f}, {S.max():.2f}], E: [{E.min():.2f}, {E.max():.2f}], I: [{I.min():.2f}, {I.max():.2f}]")

    # plotting
    plt.figure(figsize=(10,6))
    plt.plot(t, S, label='Susceptible (ODE)', color='blue')
    plt.plot(t, E, label='Exposed (ODE)', color='orange')
    plt.plot(t, I, label='Infected (ODE)', color='red', linewidth=2)
    plt.plot(t, R, label='Recovered (ODE)', color='green')
    plt.plot(t, V, label='Vaccinated (ODE)', color='purple')

    # optionally overlay ABM results if CSV exists
    if overlay_abm and os.path.exists(abm_csv):
        try:
            df = pd.read_csv(abm_csv)
            if 'day' in df.columns and 'I' in df.columns:
                plt.plot(df['day'], df['I'], 'k--', label='ABM Infected (CSV)')
                log(f"Overlaying ABM results from {abm_csv}")
            else:
                log(f"CSV {abm_csv} found but doesn't contain 'day' and 'I' columns.")
        except Exception as e:
            log(f"Failed to load ABM CSV: {e}")

    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SEIRV ODE Validation")
    plt.legend()
    plt.grid(True)

    log("Validation complete — showing plot.")
    plt.show()

    total_population = S + E + I + R + V
    if not np.allclose(total_population, N, atol=1e-2):
        log(f"Warning: Population not conserved. Range: [{total_population.min():.2f}, {total_population.max():.2f}]")
    else:
        log("Population conserved throughout simulation.")

if __name__ == "__main__":
    # default run: small nonzero E0 & I0 so infection can start
    run_validation()


