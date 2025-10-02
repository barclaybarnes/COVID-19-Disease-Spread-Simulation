# validation.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import config

def seirv_model(y, t, beta, sigma, gamma, nu):
    S, E, I, R, V = y
    N = S + E + I + R + V
    dSdt = -beta * S * I / N - nu * S
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    dVdt = nu * S
    return [dSdt, dEdt, dIdt, dRdt, dVdt]

def run_seirv_ode():
    N = 1000
    y0 = [999, 1, 0, 0, 0]
    t = np.linspace(0, 200, 200)
    sol = odeint(seirv_model, y0, t, args=(config.BETA, config.SIGMA, config.GAMMA, config.NU))
    S, E, I, R, V = sol.T
    plt.plot(t, I, label="ODE Predicted Infected", linestyle='--')
    plt.legend()
