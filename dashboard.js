// Sign Out Functionality
document.getElementById('signout-button').addEventListener('click', function () {
    alert('You have been signed out.');
    window.location.href = 'index.html'; // Replace with your login page URL
});

// Add Cattle Functionality
document.getElementById('add-cattle-button').addEventListener('click', function () {
    window.location.href = 'add-cattle.html'; // Replace with your Add Cattle page URL
});

// View Cattle Details (Navigate to details page)
function viewCattle(index) {
    window.location.href = `cattle-detail.html?index=${index}`;
}

// Fetch and Display Cattle Data on Dashboard
function loadCattleData() {
    const cattleList = JSON.parse(localStorage.getItem('cattleData')) || [];
    const tableBody = document.querySelector('.styled-table tbody');
    const alertContainer = document.querySelector('.alerts');

    // Clear previous data
    tableBody.innerHTML = '';
    alertContainer.innerHTML = '<h2>Recent Alerts</h2>';

    cattleList.forEach((cattle, index) => {
        let isHealthy = true;

        // Validate required fields
        const { temperature, humidity, accelX, accelY, accelZ } = cattle;

        // Temperature: 38.6°C – 39.5°C
        if (temperature < 38.6 || temperature > 39.5) isHealthy = false;

        // Humidity: 60% – 80%
        if (humidity < 60 || humidity > 80) isHealthy = false;

        // AccelX/Y: –0.3g to +0.3g, AccelZ: 0.7g to 1.2g
        const abnormalAccel =
            accelX < -0.3 || accelX > 0.3 ||
            accelY < -0.3 || accelY > 0.3 ||
            accelZ < 0.7 || accelZ > 1.2;

        if (abnormalAccel) isHealthy = false;

        // Assign health status
        if (isHealthy) {
            cattle.status = 'Healthy';
        } else {
            // Determine severity based only on temperature
            if (temperature < 37 || temperature > 40.5) {
                cattle.status = 'Sick';
            } else {
                cattle.status = 'At Risk';
            }
        }

        // Table row
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${cattle.name}</td>
            <td><span class="status ${cattle.status.toLowerCase()}">${cattle.status}</span></td>
            <td>${cattle.lastTreatment || 'N/A'}</td>
            <td><button class="btn-view" onclick="viewCattle(${index})">View</button></td>
        `;
        tableBody.appendChild(row);

        // Alerts
        if (cattle.status === 'Sick' || cattle.status === 'At Risk') {
            const alertMessage = document.createElement('div');
            alertMessage.classList.add('alert');
            alertMessage.innerHTML = `<p><strong>Alert:</strong> Cattle "${cattle.name}" is currently ${cattle.status}. Immediate action required!</p>`;
            alertContainer.appendChild(alertMessage);
        }
    });

    // Overview stats
    document.getElementById('total-cattle').textContent = cattleList.length;
    document.getElementById('healthy-cattle').textContent = cattleList.filter(c => c.status === 'Healthy').length;
    document.getElementById('sick-cattle').textContent = cattleList.filter(c => c.status === 'Sick').length;
    document.getElementById('at-risk-cattle').textContent = cattleList.filter(c => c.status === 'At Risk').length;
}

// Load on page ready
document.addEventListener('DOMContentLoaded', loadCattleData);
