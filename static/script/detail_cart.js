function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
 }
 
 function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    
 }

 $("#main").click(function(){
       $("#navbarSupportedContent").toggleClass("nav-normal")
 })
function updateInputFields() {
    var selectedOption = document.getElementById("address-dropdown").value;
    var selectedAddress = selectedOption.split(', '); // Splitting the selected option by comma and space

    // Updating input field values with the selected address details
    document.getElementById('province').value = selectedAddress[0];
    document.getElementById('city').value = selectedAddress[1];
    document.getElementById('detail').value = selectedAddress[2];
    document.getElementById('post_code').value = selectedAddress[3];
}
const accessToken = localStorage.getItem('access_token');
const url='/order/api'+window.location.pathname
fetch(url,{
  method:"GET",
  headers:{
  "Content-Type":"application/json",
  "Authorization":"JWT "+accessToken
  }
  })
.then(response => response.json())
.then(data => {
    // Replace the innerHTML of the elements with the data from the API
    console.log(data.total_price)
    document.getElementById('username').innerHTML = 'Thanks for your Order '+data.queryset.user.first_name;
    document.getElementById('total-price').innerHTML = 'total price: '+data.queryset.total_price;
    document.getElementById('created-at').innerHTML = 'created at '+data.queryset.created_at;
    document.getElementById('Paid').innerHTML = 'is paid: '+data.queryset.is_paid;
    document.getElementById('Coupon').innerHTML = 'coupon: '+data.queryset.coupon;
    document.getElementById('total-paid').innerHTML = data.queryset.total_price;
    document.getElementById('province-detail').innerHTML = 'province: '+data.queryset.province;
    document.getElementById('city-detail').innerHTML = 'city: '+data.queryset.city;
    document.getElementById('detailed').innerHTML = 'address detail: '+data.queryset.detailed_address;
    document.getElementById('postal-detail').innerHTML = 'postal code: '+data.queryset.postal_code;

})
.catch(error => console.error('Error:', error));

function validateForm() {
  var province = document.getElementById('province').value;
  var city = document.getElementById('city').value;
  var detail = document.getElementById('detail').value;
  var post_code = document.getElementById('post_code').value;
  var error = false;

  if (province == "") {
      document.getElementById('provinceError').innerHTML = 'Please enter Province';
      error = true;
  }
  if (city == "") {
      document.getElementById('cityError').innerHTML = 'Please enter City';
      error = true;
  }
  if (detail == "") {
      document.getElementById('detailError').innerHTML = 'Please enter Detail';
      error = true;
  }
  if (post_code == "") {
      document.getElementById('postalError').innerHTML = 'Please enter Postal code';
      error = true;
  }

  if (error) {
      return false;
  }
  return true;
}

// Serialize form data into a JSON object
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
  var cookie = cookies[i].trim();
  if (cookie.substring(0, name.length + 1) === (name + '=')) {
  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
  break;
  }
  }
  }
  return cookieValue;
  }
function includeAuthToken() {
  const access_token = localStorage.getItem("access_token");
  if (access_token) {
  return {
  'Authorization': 'JWT ' + access_token
  };
  }
  return {};
  }
  function saveAddress() {
    var province = document.getElementById('province').value;
    var city = document.getElementById('city').value;
    var detail = document.getElementById('detail').value;
    var post_code = document.getElementById('post_code').value;

    const formData = new FormData(document.getElementById("myForm"));
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    const accessToken = localStorage.getItem('access_token');

    fetch('/order/api/address/', {
        method: 'POST',
        headers: {
            ...includeAuthToken(),
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            province: province,
            city: city,
            detailed_address: detail,
            postal_code: post_code,
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            alert('Address created successfully');
            console.log(data);
        } else {
            throw new Error('Address creation failed: ' + data.error);
        }
    })
}

fetch('/accounts/api/address/', {
method: 'GET',
headers: {
    'Content-Type': 'application/json',
    "Authorization":"JWT "+accessToken
}
})
.then(response => response.json())
.then(data => {
  const addressDropdown = document.getElementById('address-dropdown');
  data.queryset.forEach(address => {
      const option = document.createElement('option');
      option.value = `${address.province}, ${address.city}, ${address.detailed_address}, ${address.postal_code}`;
      option.text = `${address.province}, ${address.city}, ${address.detailed_address}, ${address.postal_code}`;
      addressDropdown.appendChild(option);
  });
  // Add event listener to the dropdown to update input fields on selection change
  addressDropdown.addEventListener('change', updateInputFields);
})
.catch(error => {
  console.error('Error:', error);
});
var cartLength = cart.length;
var cartLink = document.getElementById("cart-link");
cartLink.textContent = "CART " + cartLength;
document.addEventListener("DOMContentLoaded", function() {
    var loginLink = document.getElementById('loginLink');
    var logoutLink = document.getElementById('logoutLink');

    // Check if access token exists in localStorage
    if (localStorage.getItem('access_token')) {
       // Access token exists, hide login link and show logout link
       loginLink.style.display = 'none';
       logoutLink.style.display = 'block';
    } else {
       // Access token doesn't exist, show login link and hide logout link
       loginLink.style.display = 'block';
       logoutLink.style.display = 'none';
    }
});

// Function to logout and remove access token from localStorage
function logoutFunc() {
    localStorage.removeItem("access_token");
    window.location.reload(); // Reload the page to reflect changes
}