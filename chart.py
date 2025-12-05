import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Synthetic data
np.random.seed(42)
n = 120
df = pd.DataFrame({
    "acquisition_cost": np.random.uniform(20, 150, n),
    "lifetime_value": np.random.uniform(200, 2000, n),
    "segment": np.random.choice(["New", "Returning", "VIP"], n)
})

# Create EXACT pixel figure:
# 512px / 64 DPI = 8 inches → figure must be (8, 8)
fig = plt.figure(figsize=(8, 8), dpi=64)

# Disable autoscaling that alters size
fig.set_tight_layout(False)

# Create axes without automatic resizing
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

sns.scatterplot(
    data=df,
    x="acquisition_cost",
    y="lifetime_value",
    hue="segment",
    palette="viridis",
    s=80,
    ax=ax
)

ax.set_title("Customer Lifetime Value vs Acquisition Cost", fontsize=16)
ax.set_xlabel("Acquisition Cost ($)")
ax.set_ylabel("Lifetime Value ($)")

# Save EXACT 512×512 — no bbox_inches!
fig.savefig("chart.png", dpi=64)

plt.close()
