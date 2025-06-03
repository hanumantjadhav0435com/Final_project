import numpy as np
import pickle
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Load the trained SVM model
with open("svm_cattle_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Check if the model supports probability predictions
supports_proba = hasattr(model, "predict_proba")

CSV_FILE = "cattle_data.csv"  # Path to live sensor data file

# Function to read the latest sensor data from CSV
def get_latest_sensor_data():
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            return None
        latest_data = df.iloc[-1].to_dict()  # Get the last row
        return latest_data
    except Exception as e:
        print("❌ Error reading CSV file:", e)
        return None

# API Endpoint to Predict Health Status
@app.route("/predict", methods=["GET"])
def predict():
    try:
        sensor_data = get_latest_sensor_data()
        if not sensor_data:
            return jsonify({"error": "No valid sensor data available"}), 400

        required_fields = ["Temperature", "Humidity", "HeartRate", "AccelX", "AccelY", "AccelZ"]
        if not all(field in sensor_data for field in required_fields):
            return jsonify({"error": "Missing required sensor fields"}), 400

        # Prepare data for model
        features = np.array([[
            sensor_data["Temperature"],
            sensor_data["Humidity"],
            sensor_data["HeartRate"],
            sensor_data["AccelX"],
            sensor_data["AccelY"],
            sensor_data["AccelZ"]
        ]])

        # Predict (0 = Unhealthy, 1 = Healthy)
        prediction = model.predict(features)[0]
        probability = None

        # Get probability only if model supports it
        if supports_proba:
            probability = model.predict_proba(features)[0][1] * 100  # Probability of being Healthy

        result = {
            "health_status": "Healthy" if prediction == 1 else "Unhealthy",
            "probability": round(probability, 2) if probability is not None else "N/A",
            "sensor_data": sensor_data
        }
        print(f"🔮 Prediction: {result}")

        return jsonify(result)

    except Exception as e:
        print("❌ Prediction Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
