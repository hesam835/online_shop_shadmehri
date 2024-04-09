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

  function fetchProductDetail() {
      fetch('/api' + window.location.pathname)
      .then(response => response.json())
          .then(product => {
              const productDetailContainer = document.getElementById('productDetailContainer');

              const colDiv = document.createElement('div');
              colDiv.classList.add('col-md-7');

              const laptopImg = document.createElement('div');
              laptopImg.classList.add('laptop1_img');
              laptopImg.innerHTML = `<figure><img src="${product.product.image}" alt="${product.product.name}" class="cycle1-img"/></figure>`;
              colDiv.appendChild(laptopImg);

              const colDiv2 = document.createElement('div');
              colDiv2.classList.add('col-md-5');

              const titlePage = document.createElement('div');
              titlePage.classList.add('titlepage');
              titlePage.innerHTML = `
                  <h2>${product.product.name}</h2>
                  <h1>${product.product.brand}</h1>
                  <div class="product-info">
                      <div><strong>Description:</strong> ${product.product.description}</div>
                      <div><strong>Price:</strong> ${product.product.price}</div>
                      <div><strong>Inventory quantity:</strong> ${product.product.inventory_quantity}</div>
                      <div><strong>Discount:</strong> ${product.discounts.value ? product.discounts.value : '-'}%</div>
                      <div><strong>price:</strong> ${product.product.price}$</div>
                      <div><strong>brand:</strong> ${product.product.brand}</div>

                    <div class="container mt-5">
                       <form id="myForm" class="needs-validation" novalidate action="/order/api/cart_add/${product.product.slug}/" method="post">
                           <div class="form-group">
                               <label for="myInput">Enter an Integer:</label>
                               <input type="number" class="form-control" id="myInput" name="myInput">
                               <div class="invalid-feedback">
                                   Please enter a valid integer.
                               </div>
                           </div>
                           <button type="submit" class="btn btn-primary">Submit</button>
                       </form>
                   </div>
                    <a class="read_more" href="/comment/${product.product.slug}">comment</a>>

               </div>
              `;
              colDiv2.appendChild(titlePage);

              productDetailContainer.appendChild(colDiv);
              productDetailContainer.appendChild(colDiv2);
          })
          .catch(error => console.error('Error fetching product detail:', error));
  }

  window.addEventListener('DOMContentLoaded', fetchProductDetail);
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