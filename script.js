document.getElementById('login-form').addEventListener('submit', function (event) {
  event.preventDefault();

  const enteredUsername = document.getElementById('username').value.trim();
  const enteredPassword = document.getElementById('password').value;
  const errorMessage = document.getElementById('error-message');

  // Retrieve credentials from localStorage
  const savedUsername = localStorage.getItem('username');
  const savedPassword = localStorage.getItem('password');

  // Validate login credentials
  if (enteredUsername === savedUsername && enteredPassword === savedPassword) {
    alert('Login successful! Redirecting to dashboard...');
    window.location.href = 'dashboard.html'; // Redirect to dashboard
  } else {
    errorMessage.style.display = 'block';
    errorMessage.textContent = 'Invalid username or password.';
    setTimeout(() => {
      errorMessage.style.display = 'none';
    }, 3000);
  }
});

// Redirect to signup page
document.getElementById('signup-button').addEventListener('click', function () {
  window.location.href = 'signup.html';
});
