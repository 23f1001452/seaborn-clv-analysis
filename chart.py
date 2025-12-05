import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
np.random.seed(42)
n = 120
df = pd.DataFrame({
    "acquisition_cost": np.random.uniform(20, 150, n),
    "lifetime_value": np.random.uniform(200, 2000, n),
    "segment": np.random.choice(["New", "Returning", "VIP"], n)
})

# Figure size for EXACT 512x512 output:
# DPI = 64, FIGSIZE = (8, 8)  →  8 inches * 64 dpi = 512 pixels
plt.figure(figsize=(8, 8), dpi=64)

# Scatterplot
sns.scatterplot(
    data=df,
    x="acquisition_cost",
    y="lifetime_value",
    hue="segment",
    palette="viridis",
    s=80
)

plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16)
plt.xlabel("Acquisition Cost ($)")
plt.ylabel("Lifetime Value ($)")

# Save with exact dimensions
plt.savefig("chart.png", dpi=64, bbox_inches="tight", pad_inches=0)

plt.close()
