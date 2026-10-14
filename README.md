# PopuDynamics — Mathematical Population Growth Model

A Python-based mathematical modelling project that simulates and compares population growth using exponential and logistic differential equation models.

## Overview

PopuDynamics explores how populations evolve over time under different growth assumptions. It implements two classical mathematical models to understand unrestricted population growth and growth under resource constraints.

The project uses Python, NumPy, and Matplotlib to calculate population trajectories and visualize the differences between these models.

## Mathematical Models

### 1. Exponential Growth Model

The exponential model assumes that the population grows at a constant proportional rate without resource limitations.

**Differential equation:**

$$
\frac{dP}{dt} = rP\left(1-\frac{P}{K}\right)
$$

**Analytical solution:**

$$
P(t) = \frac{K}{1+\left(\frac{K-P_0}{P_0}\right)e^{-rt}}
$$

Where:
- \(P(t)\): Population at time \(t\)
- \(P_0\): Initial population
- \(r\): Intrinsic growth rate
- \(t\): Time elapsed

### 2. Logistic Growth Model

The logistic model incorporates a carrying capacity, representing the population level at which growth approaches equilibrium.

**Differential equation:**

\[
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)
\]

**Analytical solution:**

\[
P(t)=\frac{K}{1+\left(\frac{K-P_0}{P_0}\right)e^{-rt}}
\]

Where:
- \(K\): Carrying capacity
- \(P_0\): Initial population
- \(r\): Intrinsic growth rate
- \(t\): Time elapsed

Unlike exponential growth, logistic growth slows as the population approaches its carrying capacity.

## Features

- Mathematical implementation of exponential population growth.
- Logistic population growth with a carrying capacity.
- Comparison of two population growth models.
- Visualization of population trajectories using Matplotlib.
- Configurable initial population, growth rate, and carrying capacity.
- Automatic saving of the generated graph.

## Tech Stack

- **Python** — Core implementation
- **NumPy** — Numerical computation
- **Matplotlib** — Data visualization
- **SciPy** — Planned parameter estimation and optimization
- **Pandas** — Planned demographic data analysis

## Project Structure

```text
PopuDynamics/
├── src/
│   └── models.py
├── results/
│   └── population_growth.png
├── main.py
├── requirements.txt
└── README.md
```

## Installation and Usage

### Prerequisites

- Python 3.10 or later recommended
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PopuDynamics.git
cd PopuDynamics
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the simulation

```bash
python main.py
```

The program displays the population growth comparison graph and saves it to `results/population_growth.png`.

## Example Parameters

The initial simulation uses illustrative parameters:

| Parameter | Value |
|---|---:|
| Initial population (\(P_0\)) | 1,000 |
| Growth rate (\(r\)) | 0.08 per year |
| Carrying capacity (\(K\)) | 10,000 |
| Simulation duration | 100 years |

These values demonstrate model behaviour and are not empirical estimates of a real population.

## Results and Interpretation

The simulation demonstrates two distinct behaviours:

- **Exponential growth:** Population continues increasing without an imposed resource limit.
- **Logistic growth:** Population growth slows as it approaches the carrying capacity.

The comparison illustrates how mathematical assumptions influence long-term population projections.

## Limitations

- The initial simulation uses hypothetical parameters.
- The models do not explicitly account for migration, fertility changes, mortality changes, or demographic policy.
- Carrying capacity is assumed constant in the logistic model.
- Predictions should not be interpreted as validated real-world population forecasts.

## Future Improvements

- Integrate historical population data from the World Bank or United Nations.
- Estimate growth parameters from observed demographic data.
- Compare predictions with held-out historical observations.
- Evaluate model performance using MAE and RMSE.
- Explore age-structured population models and time-varying growth rates.
- Build an interactive population growth simulator.

## Learning Objectives

This project explores the application of differential equations, mathematical modelling, numerical computation, and scientific visualization to population dynamics.

## References

- [OpenStax — The Logistic Equation](https://openstax.org/books/calculus-volume-2/pages/4-4-the-logistic-equation)
- [World Bank — Population, Total](https://data.worldbank.org/indicator/SP.POP.TOTL)
- [United Nations — World Population Prospects](https://population.un.org/wpp/)

## Author

**Archit Dubey**

B.Tech Mathematics & Computing

Interested in mathematical modelling, scientific computing, and data-driven research.

## License

This project is intended for educational and research purposes. A license can be added to define the terms under which others may use and modify the code.
