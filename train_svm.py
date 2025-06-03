import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle

# 1️⃣ Load Data
try:
    data = pd.read_csv("cattle_data.csv")  # Ensure file exists
except FileNotFoundError:
    print("❌ Error: 'cattle_data.csv' not found!")
    exit()

# 2️⃣ Handle Missing Values
data.dropna(inplace=True)

# 3️⃣ Features & Labels
X = data[['Temperature', 'Humidity', 'HeartRate', 'AccelX', 'AccelY', 'AccelZ']]
y = data['HealthStatus']

# Ensure `HealthStatus` is binary (0 = Unhealthy, 1 = Healthy)
if not set(y.unique()).issubset({0, 1}):
    print("❌ Error: HealthStatus must be 0 or 1!")
    exit()

# 4️⃣ Standardize Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5️⃣ Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 6️⃣ Train SVM Model
svm_model = SVC(kernel='rbf', probability=True)
svm_model.fit(X_train, y_train)

# 7️⃣ Evaluate Model
y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ SVM Model Accuracy: {accuracy * 100:.2f}%")

# 8️⃣ Save Model & Scaler
with open("svm_cattle_model.pkl", "wb") as model_file:
    pickle.dump(svm_model, model_file)

with open("scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file)

print("✅ SVM Model & Scaler Saved!")
