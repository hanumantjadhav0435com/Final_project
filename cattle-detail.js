// Function to load and display cattle details
document.addEventListener('DOMContentLoaded', () => {
    // Get the cattle index from the URL query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const cattleIndex = parseInt(urlParams.get('index'), 10);
  
    // Retrieve cattle data from localStorage
    const cattleList = JSON.parse(localStorage.getItem('cattleData')) || [];
  
    if (cattleList[cattleIndex]) {
      // Populate form fields with the cattle's data
      const cattle = cattleList[cattleIndex];
      document.getElementById('cattle-name').value = cattle.name || '';

      document.getElementById('cattle-temperature').value = cattle.temperature || '';
      document.getElementById('cattle-humidity').value = cattle.humidity || '';
      document.getElementById('cattle-accelerometer').value = cattle.accelerometer || '';
      document.getElementById('cattle-treatment').value = cattle.lastTreatment || '';
    } else {
      alert('No data found for the selected cattle.');
    }
  
    // Handle the update button click
    document.getElementById('update-button').addEventListener('click', () => {
      const updatedTemperature = document.getElementById('cattle-temperature').value;
      const updatedHumidity = document.getElementById('cattle-humidity').value;
      const updatedTreatment = document.getElementById('cattle-treatment').value;
  
      // Update cattle data
      if (cattleList[cattleIndex]) {
        cattleList[cattleIndex].temperature = parseFloat(updatedTemperature);
        cattleList[cattleIndex].humidity = parseFloat(updatedHumidity);
        cattleList[cattleIndex].lastTreatment = updatedTreatment;
  
        // Save updated data back to localStorage
        localStorage.setItem('cattleData', JSON.stringify(cattleList));
  
        alert('Cattle details updated successfully!');
        window.location.href = 'dashboard.html';
      } else {
        alert('Failed to update cattle details.');
      }
    });
  });
  