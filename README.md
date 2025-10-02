This project develops an agent-based simulation of COVID-19 using the SEIRV (Susceptible, Exposed, Infected, Recovered, Vaccinated) framework.
Each agent represents an individual with personal attributes such as mask use and vaccination status.
Agents interact randomly each day, and transmission occurs probabilistically according to calibrated parameters from published research.
The model extends the classical SEIR equations to a stochastic environment, capturing variability and uncertainty in epidemic outcomes.

Implemented in Python, the simulation logs population states over time, visualizes infection curves, and validates its behavior against an analytical SEIRV differential-equation model.
Multiple runs support statistical averaging to evaluate intervention effectiveness.

This tool provides a flexible platform for exploring the impact of preventive measures, vaccination rates, and transmission parameters on epidemic dynamics.
It is designed for educational, analytical, and research use in studying infectious-disease spread.

Implemented

SEIRV Agent-Based Model

Random contact mechanism

Parameter calibration (β, e_m, e_v)

CSV logging and Matplotlib visualization

ODE validation framework

Stochastic multi-run analysis

References

Kermack, W.O., & McKendrick, A.G. (1927). A Contribution to the Mathematical Theory of Epidemics.

Ferguson et al. (2020). Impact of Non-Pharmaceutical Interventions (Imperial College COVID-19 Response Team).

Chu et al. (2020). Physical distancing, face masks, and eye protection to prevent transmission of SARS-CoV-2.

Bubar et al. (2021). Model-informed COVID-19 vaccine prioritization strategies.

Allen, L. (2017). A Primer on Stochastic Epidemic Models.

Giordano et al. (2020). Modelling the COVID-19 epidemic and implementation of population-wide interventions.

Barclay Barnes
College of Computing and Software Engineering
Kennesaw State University
Email: bbarne74@students.kennesaw.edu

Quick Run Reference
python main.py          # Run single simulation
python -m validation    # Compare with SEIRV ODE
python run_multiple.py  # Multi-run stochastic average
