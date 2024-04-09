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

document.getElementById("myForm-register").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    // Call the registerFunc() function to handle form submission
    Register();

});

function Register() {
    const formData = new FormData(document.getElementById("myForm-register"));
    const data = {
        first_name: formData.get('first_name'),
        last_name: formData.get('last_name'),
        email: formData.get('email'),
        phone_number: formData.get('phone_number'),
        password: formData.get('password')
    };
    fetch('/accounts/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(data => {

        alert('We sent to your email an OTP code');

        window.location.href = '/accounts/verify_code/';

    })

    .catch(error => {

        console.error('Error:', error); 

        alert(error);

        window.location.reload();

    });
}