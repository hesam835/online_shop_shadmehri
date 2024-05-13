fetch('/api'+window.location.pathname ,{
    method:"GET",
    headers:{
    "Content-Type":"application/json",
    }
    })
.then(response => response.json())
.then(data => {
    const productList = document.getElementById('comment-list');
    productList.innerHTML = '';

    data.comment.forEach(function (product) {
        const commentContainer = document.createElement('div');
        commentContainer.classList.add('be-comment');

        commentContainer.innerHTML = `
        <div class="be-comment-content">
            <div class="be-img-comment">    
                <a href="blog-detail-2.html">
                    <img src="${product.user_id.image}" alt="" class="be-ava-comment">
                </a>
            </div>    
            <span class="be-comment-name">
                <a href="blog-detail-2.html">${product.user_id.first_name}</a>
                </span>
            <span class="be-comment-time">
                <i class="fa fa-clock-o"></i>
                ${product.created_at}
            </span>
            <p class="be-comment-text">
                ${product.text_message}
            </p>
        </div>
        
        `;
        
        productList.appendChild(commentContainer);
    });
})
.catch(error => console.error('Error:', error)); 

    const submitButton = document.querySelector('.btn-primary');

    submitButton.addEventListener('click', function() {
        const nameInput = document.querySelector('input[placeholder="Your name"]');
        const emailInput = document.querySelector('input[placeholder="Your email"]');
        const commentInput = document.querySelector('textarea[placeholder="Your text"]');
        
        const newComment = {
            name: nameInput.value,
            email: emailInput.value,
            text_message: commentInput.value
        };

        fetch('/api'+window.location.pathname, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newComment)
        })
        .then(response => response.json())
        .then(data => {
            console.log('New comment added:', data);
            window.location.reload();
        })
        .catch(error => console.error('Error:', error));
        window.location.reload();
    });
;
var cartLength = cart.length;
var cartLink = document.getElementById("cart-link");
cartLink.textContent = "CART " + cartLength;