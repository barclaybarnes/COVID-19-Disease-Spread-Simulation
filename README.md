COVID-19 Agent-Based Simulation (SEIRV)

This project implements an agent-based SEIRV (Susceptible–Exposed–Infected–Recovered–Vaccinated) model of COVID-19 using Python.
The simulation represents individuals as agents who interact under probabilistic rules, allowing exploration of mask usage, vaccination rates, and stochastic variability in disease spread.
It compares Agent-Based Model (ABM) results against deterministic SEIR differential equations (ODEs) for validation.

Project Overview

The model extends classical SEIR equations into a probabilistic agent-based environment.
Each agent has individual attributes such as:

Infection state (S, E, I, R, V)

Mask usage

Vaccination status

Agents meet other agents randomly each day, and infections occur with probability:
P(infection) = β × (1 - e_m) × (1 - e_v)

where:

β = base transmission probability

e_m = mask effectiveness

e_v = vaccine effectiveness

This setup enables simulation of different intervention strategies and their impact on outbreak dynamics.

Installation
Prerequisites

Python 3.10 or higher

Git

Clone Repository
git clone https://github.com/<your-username>/covid19-simulation.git
cd covid19-simulation

Install Dependencies
pip install -r requirements.txt

Project Structure
covid19_simulation/
│
├── agent.py              # Agent class (S, E, I, R, V)
├── environment.py        # Population generation and random mixing
├── simulation.py         # SEIRV logic and daily transitions
├── data_collector.py     # Data collection and CSV export
├── visualization.py      # Epidemic curve plotting
├── validation.py         # ODE SEIRV model comparison
├── run_multiple.py       # Multi-run stochastic analysis
├── config.py             # Parameter calibration
├── main.py               # Simulation entry point
│
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── .gitignore            # Ignore caches, CSV, IDE files

Usage
Run a Single Simulation

Runs one SEIRV agent-based simulation and plots epidemic curves.

python main.py


Output:

Saves simulation_results.csv

Displays infection curve plot

Validate Against Theoretical SEIRV (ODE)

Compares ABM results to a differential-equation SEIRV model.

python -m validation


Displays ODE-predicted infected curve for verification.

Run Multiple Simulations (Stochastic Analysis)

Runs the model multiple times and computes mean and standard deviation of infections.

python run_multiple.py


Displays a shaded uncertainty plot (mean ± std. deviation).

Parameter Specification
Parameter	Description	Source	Value
β	Transmission rate	Ferguson et al. (2020)	0.10
e_m	Mask effectiveness	Chu et al. (2020)	0.60
e_v	Vaccine effectiveness	Bubar et al. (2021)	0.85
σ	Incubation rate (1/5 days)	WHO	0.20
γ	Recovery rate (1/7 days)	Ferguson et al.	0.14
ν	Vaccination rate	Bubar et al. (2021)	0.02

These calibrated parameters reflect real-world COVID-19 research values.

Architecture Overview

The system follows an agent-based architecture with object-oriented modularity:

Component	Description
Agent	Represents an individual with health state, mask, vaccine
Environment	Holds the entire population, defines contact rules
Simulation	Core SEIRV logic controlling infection and recovery
DataCollector	Records population states each day
Visualization	Plots results using Matplotlib
Validation	SEIRV ODE comparison for model verification

Refer to UML diagrams (Class and Sequence) for structure and process flow.

Validation Strategy

The ABM results are validated via:

Comparative Validation: Using the SEIRV ODE system solved via SciPy’s odeint to confirm infection curve trends.

Empirical Validation: Comparing simulated outbreak shapes to early COVID-19 data.

Stochastic Replication: Running multiple iterations to measure variability and ensure consistency.

Stochastic Analysis

To account for randomness, the simulation supports multiple runs:

Ī(t) = (1/N) Σ I_r(t)

Mean and standard deviation are visualized to display uncertainty across stochastic trials.

Output Files
File	Description
simulation_results.csv	Daily counts of S, E, I, R, V
infection_curve.png	Epidemic curve plot (Matplotlib)
validation_plot.png	Comparison of ABM vs SEIRV ODE
stochastic_plot.png	Multi-run averaged infection curve
Project Status
Implemented

Agent-based SEIRV core model

Random contact mechanism

Calibrated parameters (β, e_m, e_v)

CSV logging and Matplotlib plotting

ODE-based validation framework

Multi-run stochastic analysis

Upcoming Enhancements

JSON input for configurable parameters

Graph-based contact structure using networkx

GUI for simulation control

Integration with real data (Johns Hopkins COVID dataset)

Future Work

Extend contact structure to social networks

Add quarantine, testing, and lockdown interventions

Optimize performance for larger populations

Incorporate spatial mobility and geography

References

Kermack, W.O., & McKendrick, A.G. (1927). A Contribution to the Mathematical Theory of Epidemics.

Ferguson et al. (2020). Impact of non-pharmaceutical interventions (Imperial College COVID-19 Response Team).

Chu et al. (2020). Physical distancing, face masks, and eye protection to prevent person-to-person transmission of SARS-CoV-2.

Bubar et al. (2021). Model-informed COVID-19 vaccine prioritization strategies.

Allen, L. (2017). A Primer on Stochastic Epidemic Models.

Giordano et al. (2020). Modelling the COVID-19 epidemic and implementation of population-wide interventions.
