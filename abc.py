import pickle
import numpy as np

# Load trained SVM model
with open("svm_cattle_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Test a sample input (modify values)
test_input = np.array([[37.5, 33, 33, -1, -1, -1]])  # Example sensor data

prediction = model.predict(test_input)[0]
probability = model.predict_proba(test_input)[0][1] * 100

print("Prediction:", "Healthy" if prediction == 1 else "Unhealthy")
print("Probability of being Healthy:", round(probability, 2), "%")
