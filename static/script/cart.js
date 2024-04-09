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
  fetch('/order/api/show_cart/')
   .then(response => response.json())
   .then(data => {
       const cart = data.cart;
       const tbody = document.getElementById('cart-items');
       let totalPrice = 0; // Initialize total price variable

       cart.forEach(item => {
           const product = item.product.fields;
           const tr = document.createElement('tr');
           tr.innerHTML = `
               <td>${product.name}</td>
               <td>${item.quantity}</td>
               <td>${product.price}$</td>
               <td>${item.total_price}$</td>
               <td><button class="btn btn-primary"><a style='color:white;text-decoration: none' href="api/cart_remove/${item.product.slug}">delete</a></button></td>
           `;
           tbody.appendChild(tr);

           totalPrice += parseInt(item.total_price); // Add item's total price to total price
       });

       // Update the total price
       const total = document.getElementById('total-price');
       total.textContent = totalPrice;
   });


    // Check if the user is logged in


// Function to check if the user is logged in
function isLoggedIn() {
    // Implement your logic to check if the user is logged in
    // For example, you can check if there's a token stored in localStorage
    return localStorage.getItem('accessToken') == null;
}
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
document.getElementById('checkout-btn').addEventListener('click', function(event) {
event.preventDefault(); // Prevent the default behavior of the link
// Check if the user is logged in
  // If logged in, proceed with checkout
  fetch('/order/create_checkout', {
      method: 'GET',
      headers: {
          'Authorization': 'JWT ' + localStorage.getItem('access_token'),
          'Content-Type': 'application/json',
      },
      redirect: 'follow'
  })
  .then(response =>response.json())
  .then(data => {
      // Redirect to the order detail page upon successful creation
      window.location.href = 'order_detail/' + data.order_id; // Assuming the API returns the created order ID in JSON response
  })
  .catch(error => {
      console.error('There was a problem with your fetch operation:', error);
  });
}
);

// Function to check if the user is logged in
 function isLoggedIn() {
    // Implement your logic to check if the user is logged in
    // For example, you can check if there's a token stored in localStorage
    return localStorage.getItem('access_token') !== null;
 }
 var cartLength = cart.length;
 var cartLink = document.getElementById("cart-link");
 cartLink.textContent = "CART " + cartLength;