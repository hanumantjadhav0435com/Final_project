// Example data for the cattle health parameters
const cattleHealthData = {
  "name": "Cow 101",
  "temperature": 39.2,
  "humidity": 72,
  "accelX": 0.1,
  "accelY": -0.2,
  "accelZ": 0.95,
  "lastTreatment": "2025-05-28"
}

  
  // Function to update health data on the page
  function updateHealthData() {
    document.getElementById('temperature').textContent = `${cattleHealthData.temperature}°C`;
    document.getElementById('humidity').textContent = `${cattleHealthData.humidity}%`;
    document.getElementById('movement').textContent = cattleHealthData.accelerometer;
    document.getElementById('alert-message').textContent = cattleHealthData.healthAlert;
  }
  
  // Call the function to populate data when the page loads
  window.onload = updateHealthData;
  