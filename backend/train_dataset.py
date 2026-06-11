import pandas as pd
import numpy as np

# Generate synthetic dataset
np.random.seed(42)
data = pd.DataFrame({
    "glucose": np.random.randint(70, 200, 500),
    "haemoglobin": np.random.uniform(10, 18, 500),
    "cholesterol": np.random.randint(150, 300, 500)
})

# Label based on simple rules
def risk_label(row):
    if row["glucose"] > 126 or row["cholesterol"] > 240:
        return "High Risk"
    elif row["haemoglobin"] < 12:
        return "Moderate Risk"
    else:
        return "Normal"

data["label"] = data.apply(risk_label, axis=1)

# Save dataset
data.to_csv("synthetic_health_data.csv", index=False)
print("Synthetic dataset saved as synthetic_health_data.csv")
