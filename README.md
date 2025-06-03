🐄 Cattle Health Monitoring System

📖 Description
The **Cattle Health Monitoring System** is an end-to-end IoT and Machine Learning-based solution designed to monitor the health status of cattle in real time. It uses various sensors (DHT11 for temperature and humidity, ADXL345 for activity, and a heart rate sensor) connected via the ESP8266 microcontroller. Sensor data is transmitted to a cloud platform (ThingSpeak) and analyzed using a machine learning model (e.g., SVM) to classify cattle health as **healthy** or **unhealthy**. Alerts are generated when abnormal health patterns are detected, enabling timely intervention by farmers or veterinarians.

 ⚙️ Installation

  Follow these steps to set up and run the project locally:

1. **Clone the Repository**
 
 ```bash
 
 git clone https://github.com/your-username/cattle-health-monitoring.git

cd cattle-health-monitoring

Set Up a Virtual Environment 

python -m venv venv

source venv/bin/activate  # For Linux/macOS

venv\Scripts\activate     # For Windows

Install Python Dependencies

Make sure you have Python 3.7+ installed.

pip install -r requirements.txt

Configure Environment Variables

Create a .env file to store your API keys, ThingSpeak channel IDs, or database URIs as needed:

THINGSPEAK_API_KEY=your_key

Run the Flask Application

python server.py



🚀 Usage

Once the application is running, you can:

Open your browser and go to http://localhost:5000 to access the main dashboard.

View real-time sensor data (temperature, humidity, heart rate, and activity levels).

Monitor live predictions of cattle health status (Healthy or Unhealthy).

Receive alerts or notifications if any abnormal readings are detected.

Analyze historical data to understand trends and patterns in cattle health.

📊 Features

Real-time IoT data collection from multiple sensors

Integration with ThingSpeak for cloud-based data storage

Machine Learning-based health classification using SVM

Alert system for abnormal health detection

Clean and user-friendly web dashboard using Flask

Optional database logging for historical analysis

🛠️ Technologies Used

Python (Flask, Pandas, Scikit-learn)

ESP8266 Microcontroller

DHT11, ADXL345, Heart Rate Sensor

ThingSpeak for cloud integration

HTML/CSS/JS for frontend dashboard

🤝 Contributing

Contributions are welcome! If you'd like to improve the system or add features:

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature-name)

Open a Pull Request



📬 Contact

 Developed by Team_16

📧 Email: hanumantjadhav0435@gmail.com




