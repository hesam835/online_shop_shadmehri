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
  async function login(event) {
   event.preventDefault(); // Prevent the default form submission behavior

   const phone_number = document.getElementById('phone_number').value;
   const password = document.getElementById('password').value;

   // Validate phone number
   if (!phone_number.match(/^\d{11}$/)) {
       alert('Please enter a valid 11-digit phone number.');
       return;
   }


   try {
       const response = await fetch('/auth/jwt/create/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({ phone_number, password }),
       });

       if (response.ok) {
           const responseData = await response.json();
           const authToken = responseData.refresh;  // Change access to auth_token
           const accessToken = responseData.access;  // Change access to auth_token
           localStorage.setItem('refresh_token', authToken);  // Change access_token to auth_token
           localStorage.setItem('access_token', accessToken);  // Change access_token to auth_token

           const headers = new Headers();
           headers.append('Authorization', `Bearer ${accessToken}`);

           // Example: Fetching user data after login

           window.location.href = 'login';
       } else {
           const errorData = await response.json();
           const errorDetail = errorData.detail;
           alert(errorDetail);
       }
   } catch (error) {
       console.error('Error:', error);
       alert('An error occurred while processing your request.');
   }
}

document.getElementById('login-form').addEventListener('submit', login);
document.getElementById('customer-panel-btn').addEventListener('click', function(event) {
   event.preventDefault(); // Prevent the default action of the link

   // Check if the user is logged in
   if (!isLoggedIn()) {
       // If not logged in, show error message and redirect to login page
       alert('You need to login to proceed to checkout.');
       window.location.href = "{% url 'login' %}";
   } else {
       // If logged in, proceed to checkout page
       window.location.href = "{% url 'customer_panel' %}";
   }
});

// Function to check if the user is logged in
function isLoggedIn() {
   // Implement your logic to check if the user is logged in
   // For example, you can check if there's a token stored in localStorage
   return localStorage.getItem('accessToken') == null;
}
var cartLength = cart.length;
var cartLink = document.getElementById("cart-link");
cartLink.textContent = "CART " + cartLength;