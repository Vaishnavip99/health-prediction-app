import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import numpy as np

# Load synthetic dataset
df = pd.read_csv("synthetic_health_data.csv")

X = df[["glucose", "haemoglobin", "cholesterol"]]
y = df["label"]

# Train/test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "health_model.pkl")
print("Model trained and saved as health_model.pkl")

# Prediction function for FastAPI
def predict(values):
    loaded_model = joblib.load("health_model.pkl")
    return loaded_model.predict(values)
