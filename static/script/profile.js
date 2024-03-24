      // Fetch user data
      fetch('/accounts/api/profile/',{
        method: 'GET',
        headers: {
            'Authorization': 'JWT ' + localStorage.getItem('access_token'),
            'Content-Type': 'application/json',
        },
    })
          .then(response => response.json())
          .then(data => {
              // Populate placeholders
              document.getElementById('first-name').textContent = data.queryset.first_name;
              document.getElementById('last-name').textContent = data.queryset.last_name;
              document.getElementById('phone-number').textContent = data.queryset.phone_number;
              document.getElementById('user-email').textContent = data.queryset.email;
              document.getElementById('profile-image').innerHTML = `<img src=${data.queryset.image} alt="Admin" class="rounded-circle" width="150">
              <div class="mt-3">
                <h4>${data.queryset.first_name} ${data.queryset.last_name}</h4>
              </div>`;
          })
          .catch(error => console.error('Error fetching user data:', error));