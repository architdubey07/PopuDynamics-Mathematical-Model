
import numpy as np
import matplotlib.pyplot as plt

from src.models import exponential_growth, logistic_growth

# Illustrative parameters
P0 = 1000
r = 0.08
K = 10000

years = np.linspace(0, 100, 500)

exponential = exponential_growth(P0, r, years)
logistic = logistic_growth(P0, r, K, years)

plt.figure(figsize=(10, 6))
plt.plot(years, exponential, label="Exponential Model")
plt.plot(years, logistic, label="Logistic Model")
plt.axhline(K, linestyle="--", label="Carrying Capacity")

plt.title("Population Growth: Mathematical Model")
plt.xlabel("Time (years)")
plt.ylabel("Population")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("results/population_growth.png", dpi=200)
plt.show()
plt.savefig("results/population_growth.png",dpi=200)
print("Population after 100 years:")
print(f"Exponential: {exponential[-1]:,.0f}")
print(f"Logistic:    {logistic[-1]:,.0f}")
