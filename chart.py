# Author: 23f1001452@ds.study.iitm.ac.in
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Generate synthetic business data ---
np.random.seed(42)

n = 120
acquisition_cost = np.random.uniform(50, 300, n)
lifetime_value = acquisition_cost * np.random.uniform(2.5, 4.5, n) + np.random.normal(0, 50, n)

df = pd.DataFrame({
    "AcquisitionCost": acquisition_cost,
    "LifetimeValue": lifetime_value
})

# --- Seaborn styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Create the 512x512 figure ---
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px

# --- Scatterplot ---
sns.scatterplot(
    data=df,
    x="AcquisitionCost",
    y="LifetimeValue",
    palette="viridis"
)

plt.title("Customer Lifetime Value vs Acquisition Cost")
plt.xlabel("Acquisition Cost ($)")
plt.ylabel("Lifetime Value ($)")
plt.tight_layout()

# --- Save exact 512x512 PNG ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
