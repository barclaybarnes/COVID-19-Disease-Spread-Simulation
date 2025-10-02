# COVID-19-Disease-Spread-Simulation


This project is an agent-based simulation of COVID-19 spread implemented in Python. The model represents individuals as agents with attributes such as health state (susceptible, exposed, infected, recovered, vaccinated), vaccination status, mask usage, and daily contact rate. At each timestep, agents will interact, and infection can spread probabilistically depending on their states and interventions in place.

The simulation allows experimentation with different strategies, including mask compliance, vaccination coverage, and social distancing, to observe how these measures affect outbreaks and their dynamics. Key metrics such as infection peaks, outbreak duration, and total case count are tracked and visualized using epidemic curves.

The project leverages Python’s scientific libraries for computation and visualization, ensuring accessibility, flexibility, and reproducibility. By combining epidemiological models (SIR/SEIR) with computational methods, this simulation provides insight into how preventive measures alter disease trajectories and serves as a learning tool for understanding epidemic dynamics.

## Project Status
### Implemented Features
- Core SEIRV simulation framework built.
- Agent class, environment, and main simulation loop implemented.
- Two core models: basic SEIR and SEIR with vaccination.
- Data collection via dictionaries and CSV export.

### Upcoming Features
- Graphical data visualization (Matplotlib epidemic curve).
- Parameter tuning for vaccination and mask rates.

### Changes from Proposal
- Added probability adjustment for mask and vaccine effects. 
- Simplified environment from grid to population-based model for clarity.
