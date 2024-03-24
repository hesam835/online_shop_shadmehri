document.addEventListener('DOMContentLoaded', function() {
    fetch('/order/api/order_history',{
        method: 'GET',
        headers: {
            'Authorization': 'JWT ' + localStorage.getItem('access_token'),
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            data.queryset.forEach(item => {
                let row = document.createElement('tr');
                row.innerHTML = '<td>' + item.user.first_name+' '+item.user.last_name + '</td>' +
                                '<td>' + item.id + '</td>' +
                                '<td>' + item.total_price + '</td>' +
                                '<td>' + item.is_paid + '</td>'
                document.getElementById('cart-items').appendChild(row);
            });
        });
});
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
})
.catch(error => console.error('Error fetching user data:', error));