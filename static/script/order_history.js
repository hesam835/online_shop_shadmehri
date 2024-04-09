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
                                '<td>' + item.is_paid + '</td>'+
                                '<td><a href="order_detail/'+item.id+'" class="btn btn-primary">Checkout</a></td>' ;
                document.getElementById('cart-items').appendChild(row);
            });
        });
});