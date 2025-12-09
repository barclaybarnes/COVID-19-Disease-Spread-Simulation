# 🧬 COVID-19 Agent-Based Simulation (SEIRV)

This project implements an **agent-based SEIRV (Susceptible–Exposed–Infected–Recovered–Vaccinated)** model of COVID-19 using Python.

The simulation represents individuals as agents interacting under probabilistic rules, allowing exploration of **mask usage, vaccination rates, and stochastic variability** in disease spread. It also compares **Agent-Based Model (ABM)** results against deterministic SEIR differential equations (ODEs) for validation.

---

## 📘 Project Overview

The model extends classical SEIR equations into a probabilistic agent-based environment. Each agent has attributes such as:

- **Infection state:** S, E, I, R, V  
- **Mask usage**  
- **Vaccination status**

Agents meet randomly each day, and infections occur with probability:

P(infection) = β ⋅ (1 − e_m) ⋅ (1 − e_v)

Where:

- β = base transmission probability  
- e_m = mask effectiveness  
- e_v = vaccine effectiveness  

This setup enables simulation of different intervention strategies and their impact on outbreak dynamics.

---

## ✨ New Features

- Resource monitoring: background `ResourceMonitor` collects per\-process and system metrics and writes `resource_usage.csv` (requires `psutil`).
- Warm\-up of CPU counters, per\-sample error diagnostics, and stable CSV output (writes `"N/A"` when metrics are unavailable).
- Multi\-run analysis: `run_multiple.py` runs many stochastic simulations, computes mean ± std, exports `simulation_results_mean.csv`, and optionally overlays ODE results.
- Animated visualization: `animated_epidemic_curve.py` animates results from `simulation_results.csv` with interactive controls (play/pause, checkboxes, slider).
- Validation improvements: `validation.py` continues to solve ODE SEIRV via `scipy.integrate.odeint` and now reports diagnostics and overlays ABM CSV when available.
- CSV logging: all major modules export deterministic CSVs for reproducibility (`simulation_results.csv`, `simulation_results_mean.csv`, `resource_usage.csv`).
- Requirements updated: `psutil` required for resource monitoring; `python>=3.11` is listed in `requirements.txt`.

---

## 🚧 Project Status

### ✅ Implemented

- Agent\-based SEIRV core model  
- Random contact mechanism  
- Calibrated parameters (\β, e_m, e_v)  
- CSV logging and Matplotlib plotting  
- ODE\-based validation framework  
- Resource monitor with diagnostics and CSV output  
- Multi\-run batching and mean/std aggregation  
- Animated epidemic curve with interactive widgets

### 🛠️ Upcoming Enhancements

- JSON input for configurable parameters  
- Graph\-based contact structure using `networkx`  
- GUI for simulation control  
- Integration with real epidemiological data

### 💡 Future Work

- Extend contact structure to social networks  
- Add quarantine, testing, and lockdown interventions  
- Optimize performance for larger populations  
- Incorporate spatial mobility and geography  

---

## ⚙️ Installation

### Prerequisites

- Python `>=3.11`  
- Git  

### Clone Repository

```bash
git clone https://github.com/<your-username>/covid19-simulation.git
cd covid19-simulation
python -m pip install -r requirements.txt
python -m pip install psutil

## 🧱 Project Structure
```
covid19_simulation/
│
├── agent.py                      # Agent class (S, E, I, R, V)
├── environment.py                # Population generation and random mixing
├── simulation.py                 # SEIRV logic and daily transitions
├── data_collector.py             # Data collection and CSV export
├── visualization.py              # Epidemic curve plotting
├── animated_epidemic_curve.py    # Animated plot with controls
├── validation.py                 # ODE SEIRV model comparison and diagnostics
├── run_multiple.py               # Multi\-run stochastic analysis (mean/std)
├── resource_monitor.py           # Background resource sampling & CSV export
├── config.py                     # Parameter calibration
├── main.py                       # Simulation entry point (single run)
│
├── requirements.txt              # Dependencies (includes psutil)
├── README.md                     # Documentation
└── .gitignore                    # Ignore caches, CSV, IDE files
```
---

## 🧪 Usage

### 🧩 Run a Single Simulation

Runs one SEIRV agent-based simulation and plots epidemic curves.

```bash
python main.py
```
Output:

simulation_results.csv saved

Infection curve plotted

### 📈 Validate Against Theoretical SEIRV (ODE)

Compares Agent-Based Model (ABM) results to a deterministic SEIRV differential equation model.
```bash
python -m validation
```
Output:

Displays a shaded uncertainty plot (mean ± std. deviation)

Compares ODE predictions with ABM outcomes

### Run Multi-run (mean ± std) and Resource Monitor
Runs n_runs simulations, computes mean and std deviation, saves simulation_results_mean.csv, and records resource usage to resource_usage.csv.
```bash
python -m run_multiple
```

### 🧮 Parameter Specification
| Parameter | Description             | Source                 | Value |
| --------- | ----------------------- | ---------------------- | ----- |
| β         | Transmission rate       | Ferguson et al. (2020) | 0.10  |
| e_m       | Mask effectiveness      | Chu et al. (2020)      | 0.60  |
| e_v       | Vaccine effectiveness   | Bubar et al. (2021)    | 0.85  |
| σ         | Incubation rate (1/5 d) | WHO                    | 0.20  |
| γ         | Recovery rate (1/7 d)   | Ferguson et al.        | 0.14  |
| ν         | Vaccination rate        | Bubar et al. (2021)    | 0.02  |

## 🧩 Architecture Overview

The system follows an agent-based architecture with modular, object-oriented design.

| Component     | Description                                            |
| ------------- | ------------------------------------------------------ |
| Agent         | Represents an individual (health state, mask, vaccine) |
| Environment   | Holds the entire population and defines contact rules  |
| Simulation    | Core SEIRV logic controlling infection and recovery    |
| DataCollector | Records population states each day                     |
| Visualization | Plots epidemic curves using Matplotlib                 |
| Validation    | Compares ABM outputs against SEIRV ODE predictions     |

### 🔬 Validation Strategy

The ABM results are validated via:

Comparative Validation
Using the SEIRV ODE system solved via SciPy’s odeint to confirm infection curve trends.

Empirical Validation
Comparing simulated outbreak shapes to early COVID-19 data.

Stochastic Replication
Running multiple iterations to measure variability and ensure consistency.

## References

Kermack, W.O., & McKendrick, A.G. (1927). A Contribution to the Mathematical Theory of Epidemics.

Ferguson et al. (2020). Impact of Non-Pharmaceutical Interventions (Imperial College COVID-19 Response Team).

Chu et al. (2020). Physical distancing, face masks, and eye protection to prevent transmission of SARS-CoV-2.

Bubar et al. (2021). Model-informed COVID-19 vaccine prioritization strategies.

Allen, L. (2017). A Primer on Stochastic Epidemic Models.

Giordano et al. (2020). Modelling the COVID-19 epidemic and implementation of population-wide interventions.

## Project Author

Barclay Barnes
College of Computing and Software Engineering
Kennesaw State University
Email: bbarne74@students.kennesaw.edu

## Extended Project Demo Video

https://youtu.be/PyLvvBTn_oU

## Quick Run Reference
python main.py          # Run single simulation
python -m validation    # Compare with SEIRV ODE

Install Dependencies
pip install -r requirements.txt


