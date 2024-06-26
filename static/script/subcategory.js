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

  fetch('/api'+window.location.pathname)
  .then(response => response.json())
  .then(data => {
      var productList = $('#list-subcategory');
      data.subcategory.forEach(function(product) {
          productList.append('<div class="cycle_section_2 layout_padding"><div class="row"><div class="col-md-6"><div class="box_main"><h6 class="number_text">01</h6><div class="image_2"><img class="product-image" src='+product.image+'></div></div></div><div class="col-md-6"><h1 class="cycles_text">'+product.name+'</h1><p class="lorem_text">'+product.description+'</p><div class="btn_main"><div class="buy_bt"><a href="/list_product/' + product.slug + '/">product list</a></div><h4 class="price_text"> <span style=" color: #f7c17b">$</span> <span style=" color: #325662"></span></h4></div></div></div></div>');});})
          .catch(error => console.error('Error:', error));

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