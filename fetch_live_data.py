import serial
import pandas as pd
import os

# 🏷️ SERIAL CONFIGURATION (CHANGE THIS BASED ON YOUR SYSTEM)
SERIAL_PORT = "COM6"  # Change for Linux: "/dev/ttyUSB0"
BAUD_RATE = 115200
CSV_FILE = "cattle_data.csv"
STATUS_FILE = "status.txt"  # UI-readable status file

# 📌 Connect to ESP8266 Serial
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"✅ Connected to {SERIAL_PORT} at {BAUD_RATE} baud")
except Exception as e:
    print(f"❌ Error: Could not connect to serial port {SERIAL_PORT}. Exiting...")
    exit(1)

# 📝 CSV Header Definition
CSV_COLUMNS = ["Temperature", "Humidity", "HeartRate", "AccelX", "AccelY", "AccelZ", "HealthStatus"]

# 📌 Check if CSV exists, if not, create it with headers
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=CSV_COLUMNS).to_csv(CSV_FILE, index=False)
    print(f"📂 Created new file: {CSV_FILE}")

# 🚀 Start Reading Data
print("📱 Listening for data... (Press Ctrl+C to stop)")

try:
    while True:
        try:
            # 🔄 Read data from Serial
            line = ser.readline().decode("utf-8").strip()
            if not line:
                continue  # Ignore empty lines
            
            # Expected format: "temperature,humidity,heartRate,accelX,accelY,accelZ"
            values = line.split(",")
            if len(values) != 6:
                print(f"⚠ Invalid data received: {line}")
                continue

            # Convert values
            temperature = float(values[0])
            humidity = float(values[1])
            heart_rate = float(values[2])
            accel_x = float(values[3])
            accel_y = float(values[4])
            accel_z = float(values[5])

            # 📌 Health Score System
            health_score = 0  

            if 32.3 <= temperature <= 33.0:
                health_score += 1
            if heart_rate > 65:
                health_score += 1
            if abs(accel_x) < 0.7:
                health_score += 1
            if abs(accel_y) < 0.1:
                health_score += 1
            if abs(accel_z) < 1.1:
                health_score += 1

            # By default, set HealthStatus to Healthy
            health_status = 1  # Default is healthy
            
            # At least 4 conditions must be met for healthy status
            if health_score < 4:
                health_status = 0

            # Store sensor data
            sensor_data = {
                "Temperature": temperature,
                "Humidity": humidity,
                "HeartRate": heart_rate,
                "AccelX": accel_x,
                "AccelY": accel_y,
                "AccelZ": accel_z,
                "HealthStatus": health_status
            }

            # 📌 Update UI with health status
            with open(STATUS_FILE, "w") as f:
                f.write("Healthy" if health_status == 1 else "Unhealthy")

            # Print data to console
            if health_status == 1:
                print(f"🟢 Healthy: {sensor_data}")
            else:
                print(f"🔴 Unhealthy: {sensor_data}")

            # 📅 Save to CSV
            df = pd.DataFrame([sensor_data])
            df.to_csv(CSV_FILE, mode="a", header=False, index=False)

        except Exception as e:
            print(f"❌ Error processing data: {e}")

except KeyboardInterrupt:
    print("\n🛑 Stopping data logging...")
    
    # Update last recorded value to unhealthy
    try:
        df = pd.read_csv(CSV_FILE)
        if not df.empty:
            df.at[df.index[-1], "HealthStatus"] = 0  # Mark last record as unhealthy
            df.to_csv(CSV_FILE, index=False)
            print("✅ Last record updated to Unhealthy (0)!")
            with open(STATUS_FILE, "w") as f:
                f.write("Unhealthy")
        else:
            print("⚠ No records found in CSV to update.")
    except Exception as e:
        print(f"❌ Error updating last record: {e}")

finally:
    ser.close()
    print("✅ Serial connection closed.")
